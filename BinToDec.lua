-- Convet binary number to decimal number

function Menu(MenuCounter)
    if MenuCounter == 1 then
        print('\nWould you like to convert a binary number into a decimal number? (Y/N) ')
    end
    if MenuCounter > 1 then
        print('\nWould you like to convert another binary number into a decimal number? (Y/N) ')
    end
    choice = io.read()
    while choice ~= 'Y' and choice ~= 'N' do
        print('\nThat is not a valid choice. Please enter \"Y\" or \"N\". ')
        choice = io.read()
    end 
end

function GetNum()
    local UserBin = io.read()
    UserBin = tostring(UserBin):gsub("%s+", "")

    local LengthCheck = LenCheck(UserBin)
    local BinCheck = NumCheck(LengthCheck)

    while LengthCheck ~= BinCheck do
        LengthCheck = BinCheck
        LengthCheck = LenCheck(BinCheck)
        BinCheck = NumCheck(LengthCheck)
    end

    if LengthCheck == BinCheck then
        UserBin = BinCheck 
        print('\n' .. UserBin .. ' as a Decimal Number is ' .. BinToDec(UserBin))
    end
end

function LenCheck(LengthCheckNum)
    local LengthCheckNumString = tostring(LengthCheckNum)
    while string.len(LengthCheckNumString) > 8 do 
        print("\nThe binary number you entered is too long. Please limit it to 8 characters. ")
        LengthCheckNum = io.read()
        LengthCheckNumString = tostring(LengthCheckNum)
    end
    local UserBin = LengthCheckNum
    return UserBin
end

function NumCheck(CharCheckNum)
    local check = false
    while check == false do 
        for i = 1, string.len(tostring(CharCheckNum)) do
            local char = string.sub(tostring(CharCheckNum),i,i)
            if char ~= '0' and char ~= '1' then
                print("\nThat is not a binary number. Please enter only a \"0\" or a \"1\". ")
                CharCheckNum = io.read()
                check = false
                break
            end
            check = true
        end
    end
    local UserBin = CharCheckNum
    return UserBin
end

function BinToDec(UserBin)
    local Digits = {}
    local IndexCounter = 1
    local BinaryCounter = 1
    local Sum = 0
    local ReverseString = string.reverse(tostring(UserBin))
    for i = 1, string.len(ReverseString) do 
        local num = tonumber(string.sub(ReverseString, i , i))
        table.insert(Digits, i , num)
    end
    while IndexCounter <= string.len(ReverseString) do
        if Digits[IndexCounter] == 1 then
            Sum = Sum + BinaryCounter
        end
        BinaryCounter = BinaryCounter * 2
        IndexCounter = IndexCounter + 1
    end
    return Sum
end

print('Hello. Welcome to my binary to decimal number translator. ')
local MenuCounter = 1
Menu(MenuCounter)

while choice == 'Y' do
    MenuCounter = MenuCounter + 1
    print('\nEnter another binary number no longer than 8 characters: ')
    GetNum()
    Menu(MenuCounter)
end

if choice == 'N' then
    print('\nWhy not? ')
    reason = io.read()
    print('\nWell, okay then.')
    print('\nI guess you\'ll never know what that binary number is. :( ')
end
