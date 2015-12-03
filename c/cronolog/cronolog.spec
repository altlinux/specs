Name: cronolog
Version: 1.6.2
Release: alt1.qa1.1

Summary: A file rotation program for Apache.
License: GPL
Group: System/Servers

Url: http://www.%name.org
Source: http://www.%name.org/download/%name-%version.tar.gz
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Cronolog is a simple program that reads log messages from its input
and writes them to a set of output files, the names of which are
constructed using template and the current date and time.  The
template uses the same format specifiers as the Unix date command
(which are the same as the standard C strftime library function).

%prep
%setup -q -n %name-%version

%build
%configure
%make_build

%install
%makeinstall

%files
%_sbindir/*
%_man1dir/*
%_infodir/*
%doc AUTHORS ChangeLog NEWS README TODO


%changelog
* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1.qa1.1
- NMU: added BR: texinfo

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.6.2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Dec 06 2003 Alex Murygin <murygin@altlinux.ru> 1.6.2-alt1
- First build for Sisyphus.

