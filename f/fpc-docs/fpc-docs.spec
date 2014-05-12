Name:		fpc-docs
Version:	2.6.4
Release:	alt1

Summary:	Free Pascal Compiler documentation
License:	GPL
Group:		Documentation
Source:		%name.tar
URL:		http://www.freepascal.org/
BuildArch:	noarch
Packager:	Andrey Cherepanov <cas@altlinux.org>

%description
Documentation for fpc in HTML format.

%description -l ru_RU.UTF8
Документация по fpc в HTML.

%prep
%setup -q -c

%files
%doc doc/*

%changelog
* Mon May 12 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- New version

* Thu Dec 23 2010 Alexey Shentzev <ashen@altlinux.ru> 2.4.2-alt1
- Packaging ftp://ftp.freepascal.org/pub/fpc/dist/2.4.2/docs/doc-html.tar.gz for ALT Linux.
