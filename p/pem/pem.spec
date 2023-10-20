%define _unpackaged_files_terminate_build 1

Name: pem
Version: 0.7.9
Release: alt1

Summary: GNU personal expenses manager
License: GPL-3.0
Group: Office
Url: https://www.gnu.org/software/pem/

BuildArch: noarch

Source: %name-%version.tar

%description
GNU  Pem is a handy tool to help you keep track of your personal income and
expenses.

%prep
%setup
mv pem.txt example.pem
sed -i 's/pem.txt/example.pem/g' Makefile.am

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README AUTHORS ChangeLog NEWS
%_bindir/pem
%_man1dir/pem.1.xz
%_infodir/pem.info.xz
%_datadir/pem/

%changelog
* Fri Oct 20 2023 Vladislav Glinkin <smasher@altlinux.org> 0.7.9-alt1
- Initial build for ALT

