Module HelloWorld

    Sub Main()
        Dim Record2 As Student

        Console.WriteLine("Enter first name:")
        Record2.FirstName = Console.ReadLine

        Console.WriteLine("Enter last name:")
        Record2.LastName = Console.ReadLine

        Console.WriteLine("Enter ID Number:")
        Record2.IDNumber = Console.ReadLine

        Console.WriteLine("Enter Grade Number:")
        Record2.GradeLevel = Console.ReadLine
  
        Console.Clear()

        Console.WriteLine("The student's first name is " & Record2.FirstName)
        Console.WriteLine("The student's last name is " & Record2.LastName)
        Console.WriteLine("The student's ID numberis " & Record2.IDNumber)
        Console.WriteLine("The student's grade is " & Record2.GradeLevel)
    End Sub

    Public Structure Student
        Dim IDNumber As Integer
        Dim FirstName As String
        Dim LastName As String
        Dim GradeLevel As Integer
    End Structure

End Module