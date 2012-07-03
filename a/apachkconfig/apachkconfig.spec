%define apachk_conf_file	%apachk_addon_dir/defaults

Name: apachkconfig
Version: 0.1
Release: alt1

Summary: A tool for maintaining addon configuration accross different versions of Apache server 
Group: System/Servers
License: GPL


Source:  %name
Source1: readme.en.txt
Source2: %name.8
Source3: %name-defaults

Requires: bash vhosts-filesystem

BuildPreReq: vhosts-filesystem-devel

%description
Provides a simple command-line tool  for  maintaining  the
apache  addon  configuration  (e.g  /etc/httpd*/addon.d) directories by
relieving system administrators of the task  of  directly  manipulating
the numerous symbolic links in those directories.

%prep
%__cp %SOURCE1 .
 
%build


%install
###
## Create directories
#

%__install -d \
    %buildroot%apachk_addon_dir \
    %buildroot%_sbindir \
    %buildroot%_man8dir \

###
## Real install
#    

%__install -m700 %SOURCE0 %buildroot%_sbindir/%name
%__install -m644 %SOURCE2 %buildroot%_man8dir/%name.8
%__install -m600 %SOURCE3 %buildroot%apachk_addon_dir/defaults

%__subst "s:-=apachk_addon_dir=-:%apachk_addon_dir:
s:-=apachk_addon_initd=-:%apachk_addon_initd:
s:-=apachk_favours_dir=-:%apachk_favours_dir:
" %buildroot%_sbindir/%name

%files
%attr(0400,root,root) %config(noreplace) %apachk_conf_file
%attr(0700,root,root) %_sbindir/%name
%_man8dir/*
%doc readme.en.txt

%changelog
* Tue Jun 29 2004 Yury Konovalov <yurix@altlinux.ru> 0.1-alt1
- Initial build 

