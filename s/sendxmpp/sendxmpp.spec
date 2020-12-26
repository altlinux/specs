Group: Communications
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Authen/SASL.pm) perl(Net/Domain.pm) perl(Net/XMPP.pm) perl(open.pm) perl-devel
# END SourceDeps(oneline)
BuildRequires: /usr/bin/pod2man
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:	A Perl script to send XMPP messages
Name:		sendxmpp
Version:	1.24
Release:	alt1_12
License:	GPLv2
URL:		https://sendxmpp.hostname.sk/
Source:		https://github.com/lhost/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		sendxmpp-1.24-git20161113.patch
BuildRequires:	rpm-build-perl
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:	perl(ExtUtils/MakeMaker.pm), findutils
%else
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
%endif
BuildArch:	noarch
Source44: import.info

%description
Sendxmpp is a Perl script to send XMPP (Jabber) messages from the command
line, similar to what mail(1) does for mail. Messages can be sent both to
individual recipients and chat rooms.

%prep
%setup -q
%patch0 -p1 -b .git20161113

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%makeinstall_std
%if 0%{?rhel} && 0%{?rhel} <= 7
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -f {} \;
%endif
chmod -R u+w $RPM_BUILD_ROOT/*

%files
%doc Changes README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_12
- update to new release by fcimport

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_5
- new version

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Nov 20 2009 Denis Klimov <zver@altlinux.org> 0.0.8-alt2
- new version from upstream cvs repo
- remove needless -q and -n  params from setup macro
- remove Packager tag

* Wed Feb 08 2006 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1
- First build for Sisyphus.
