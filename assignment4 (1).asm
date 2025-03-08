TITLE Assignment 4    (assignment4.asm)

; Author: Marina Moger
; Course: CS 271
; Date: 3/3/25
; Description:
; This program generates an array of random integers, displays them, sorts them,
; calculates the median, and displays the sorted array.

INCLUDE Irvine32.inc

.data
    ; Welcome message
    welcome_msg     BYTE "Sorting Random Integers - Programmed by Marina Moger", 10, 
                    "This program generates random numbers in the range [lo .. hi],", 10, 
                    "displays the original list, sorts the list, calculates the median value,", 10, 
                    "and finally, displays the list sorted in descending order.", 10, 0

    ; Prompts and messages
    title_unsorted  BYTE "The unsorted random numbers:", 10, 0
    title_sorted    BYTE "The sorted list:", 10, 0
    prompt_size     BYTE "How many numbers should be generated? [10 .. 200]: ", 0
    prompt_lo       BYTE "Enter lower bound (lo): ", 0
    prompt_hi       BYTE "Enter upper bound (hi): ", 0
    prompt_again    BYTE "Would you like to go again (No=0/Yes=1)? ", 0
    invalid_input   BYTE "Invalid input", 10, 0
    median_msg      BYTE "The median is ", 0

    ; Formatting characters
    newline         BYTE 10, 0
    space           BYTE " ", 0

    ; Constants for input validation
    min_size        DWORD 10
    max_size        DWORD 200
    min_value       DWORD 1
    max_value       DWORD 999

    ; Variables to store user input
    array_size      DWORD ?   ; Store user-input array size
    lo              DWORD ?   ; Store lower bound for random numbers
    hi              DWORD ?   ; Store upper bound for random numbers
    response        DWORD ?   ; Store user response for repeating program

    ; Array storage
    array           DWORD 200 DUP(?)  ; Reserve space for up to 200 integers

.code
main PROC
    call introduction  ; Call the introduction procedure

repeat_program:
    push OFFSET array_size
    push OFFSET lo
    push OFFSET hi
    call getData       ; Get user input

    push array_size
    push lo
    push hi
    push OFFSET array
    call fillArray     ; Fill array with random numbers

    push OFFSET array
    push array_size
    push OFFSET title_unsorted
    call displayList   ; Display unsorted array

    push OFFSET array
    push array_size
    call sortList      ; Sort array in descending order

    push OFFSET array
    push array_size
    call displayMedian ; Display median

    push OFFSET array
    push array_size
    push OFFSET title_sorted
    call displayList   ; Display sorted array

    push OFFSET response
    call goAgain       ; Ask if user wants to repeat

    cmp response, 1
    je repeat_program  ; Loop if user chooses to continue

    mov eax, 0         ; Return 0 (exit success)
    ret
main ENDP


; Display welcome message
introduction PROC
    mov edx, OFFSET welcome_msg
    call WriteString
    call Crlf
    ret
introduction ENDP

; Get user input
getData PROC
    push ebp
    mov ebp, esp

    mov edi, [ebp+8]   ; Address of array_size
    mov esi, [ebp+12]  ; Address of lo
    mov ebx, [ebp+16]  ; Address of hi

size_input:
    mov edx, OFFSET prompt_size
    call WriteString
    call ReadInt
    cmp eax, min_size
    jl invalid_size
    cmp eax, max_size
    jg invalid_size
    mov [edi], eax
    jmp size_valid

invalid_size:
    mov edx, OFFSET invalid_input
    call WriteString
    call Crlf
    jmp size_input
size_valid:

lo_input:
    mov edx, OFFSET prompt_lo
    call WriteString
    call ReadInt
    cmp eax, min_value
    jl invalid_lo
    mov [esi], eax
    jmp lo_valid

invalid_lo:
    mov edx, OFFSET invalid_input
    call WriteString
    call Crlf
    jmp lo_input
lo_valid:

hi_input:
    mov edx, OFFSET prompt_hi
    call WriteString
    call ReadInt
    cmp eax, max_value
    jg invalid_hi
    cmp eax, [esi]
    jl invalid_hi
    mov [ebx], eax
    jmp hi_valid

invalid_hi:
    mov edx, OFFSET invalid_input
    call WriteString
    call Crlf
    jmp hi_input
hi_valid:

    pop ebp
    ret 12
getData ENDP

; Fill array with random numbers
fillArray PROC
    push ebp
    mov ebp, esp

    mov ecx, [ebp+8]   ; array_size
    mov eax, [ebp+12]  ; lo
    mov edx, [ebp+16]  ; hi
    mov esi, [ebp+20]  ; array address

    call Randomize

fill_loop:
    push edx
    push eax
    sub edx, eax
    inc edx
    call RandomRange
    add eax, [ebp+12]  ; Adjust to lo range
    mov [esi], eax
    add esi, 4
    loop fill_loop

    pop ebp
    ret 16
fillArray ENDP

; Sort array in descending order
sortList PROC
    push ebp
    mov ebp, esp
    ; Sorting logic (Selection Sort)
    pop ebp
    ret 8
sortList ENDP

; Display median value
displayMedian PROC
    push ebp
    mov ebp, esp
    ; Median calculation logic
    pop ebp
    ret 8
displayMedian ENDP

; Display list of numbers
displayList PROC
    push ebp
    mov ebp, esp
    ; List display logic
    pop ebp
    ret 12
displayList ENDP

; Ask user to go again
goAgain PROC
    push ebp
    mov ebp, esp

    mov edx, OFFSET prompt_again
    call WriteString
    call ReadInt
    mov edi, [ebp+8]
    mov [edi], eax

    pop ebp
    ret 4
goAgain ENDP

END main
