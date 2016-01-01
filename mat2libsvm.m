function mat2libsvm(labels, traindata, outputfile)
% Usage:
%       mat2libsvm(labels, data,file_name)
% where labels:  label vector
%       data  : data matrix
%       file_name: output filename

%  Author:  Chandresh contact: ckm.jnu@gmail.com

file = fopen(outputfile, 'w');
[i,j,val]=find(traindata);
for k = 1:length(labels)
    line = num2str(labels(k));
    idx=j(i==k);
    value=val(i==k);
    for l = 1:length(idx)      
        line = [line ' ' num2str(l) ':' num2str(value(l))];
    end
    line = [line '\n'];
    fprintf(file, line);
end

fclose(file);
end
