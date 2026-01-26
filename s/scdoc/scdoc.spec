Name: scdoc
Version: 1.11.4
Release: alt1

Summary: Tool for generating roff manual pages
License: MIT
Group: Development/Other
Url: https://git.sr.ht/~sircmpwn/scdoc
Vcs: https://git.sr.ht/~sircmpwn/scdoc

Source: %name-%version.tar

%description
scdoc is a tool designed to make the process of writing man pages more
friendly. It reads scdoc syntax from stdin and writes roff to stdout, suitable
for reading with man.

%prep
%setup

# Disable static linking
sed -i '/-static/d' Makefile

# Use INSTALL provided by the make_install macro
sed -i 's/\tinstall/\t$(INSTALL)/g' Makefile

%build
%make_build PREFIX="%_prefix"

%install
%make_install install \
	PREFIX="%buildroot%_prefix" \
	PCDIR="%buildroot%_pkgconfigdir"

%check
%make check

%files
%_bindir/%name
%_man1dir/*
%_man5dir/*
# Not shipped in a -devel package since scdoc is a development tool not
# installed in a user runtime.
%_pkgconfigdir/%name.pc

%changelog
* Mon Jan 26 2026 Ulysses Apokin <ulysses@altlinux.org> 1.11.4-alt1
- New version (1.11.4)

* Wed Dec 25 2024 Ulysses Apokin <ulysses@altlinux.org> 1.11.3-alt1
- New version (1.11.3)

* Tue Feb 08 2022 Alexey Gladkov <legion@altlinux.ru> 1.11.2-alt1
- New version (1.11.2)

* Sat Jul 17 2021 Alexey Gladkov <legion@altlinux.ru> 1.11.1-alt1
- New version (1.11.1)

* Fri Mar 27 2020 Alexey Gladkov <legion@altlinux.ru> 1.10.1-alt1
- New version (1.10.1)

* Wed May 22 2019 Alexey Gladkov <legion@altlinux.ru> 1.9.4-alt1
- Initial build.
