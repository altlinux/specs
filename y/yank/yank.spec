%define _unpackaged_files_terminate_build 1

Name: yank
Version: 1.3.0
Release: alt1
Summary: Yank terminal output to clipboard
License: MIT 
Group: Other
Url: https://github.com/mptre/yank

Source: %name-%version.tar

%description
Read input from stdin and display a selection interface that allows a field
to be selected and copied to the clipboard. Fields are either recognized by
a regular expression using the -g option or by splitting the input on a
delimiter sequence using the -d option.

%prep
%setup
sed -i '/INSTALL_PROGRAM=/s,-s,,' Makefile
sed -i '/PREFIX=/s,/usr/local,%prefix,' Makefile


%build
export CFLAGS="%optflags"
%make_build 

%install
%makeinstall_std
mkdir -p %buildroot%_man1dir
install -m 0644 %name.1* %buildroot%_man1dir

%files
%_bindir/%name
%_man1dir/%name.1*
%doc README.md LICENSE

%changelog
* Thu Feb 29 2024 Pavel Shilov <zerospirit@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus
