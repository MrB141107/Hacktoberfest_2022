package Hacktoberfest_2022.Java;
import java.util.ArrayList;
import java.util.List;

public class Letter_Combinations_of_a_Phone_Number {
    public List<String> letterCombinations(String digits) {
        if(digits.length()==0 || digits=="1")
            return new ArrayList<>();
        
        return perm("",digits);
    }
    static List<String> perm(String processed,String up){
        if(up.isEmpty()){
            List<String> list = new ArrayList<>();
            list.add(processed);
            return list;
        }
        
        List<String> list = new ArrayList<>();
        char ch = up.charAt(0);
        int di = ch-'0';
        
        int a =0;
        int b =0;
        if(di>=7){
            if(di==7){
                b=1;
            }
            if(di>7){
                a=1;
                b=1;
            }
            if(di==9)
                b++;
            
        }
        for(int i =((di-2)*3)+a ;i<((di-1)*3)+b ;i++){
            char c =(char)('a'+i);
                
            list.addAll(perm(processed+c,up.substring(1)));
        }
        return list;
            
        
    }
    
}
