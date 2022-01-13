Name:       qbe
# git log -1 --format='%as' | tr - .  
Version:    2021.12.05
Release:    alt1
Group:      Development/C
# git clone git://c9x.me/qbe.git 
# cd qbe; git archive --prefix=qbe-`git log -1 --format='%as' | tr - .`/ --output=../RPM/SOURCES/qbe-`git log -1 --format='%as' | tr - .`.tar HEAD
Source:     %name-%version.tar
License:    BSD

Summary:    C Compiler Backend
URL:        https://c9x.me/compile/
# TODO armh (buggy as for 2021.07.06)
ExclusiveArch: x86_64

%description
QBE aims to be a pure C embeddable backend that provides 70% of the
performance of advanced compilers in 10% of the code. Its small size
serves both its aspirations of correctness and our ability to
understand, fix, and improve it. It also serves its users by providing
trivial integration and great flexibility.

%prep
%setup

%build
make
make -C minic clean minic

%install
install -D obj/%name %buildroot%_bindir/%name
install -D minic/minic %buildroot%_bindir/%name-minic

%files
%doc doc README*
%_bindir/*

%check
make check

%changelog
* Wed Jan 12 2022 Fr. Br. George <george@altlinux.ru> 2021.12.05-alt1
- Version up

* Sat Aug 21 2021 Fr. Br. George <george@altlinux.ru> 2021.07.06-alt1
- Initial build for ALT
