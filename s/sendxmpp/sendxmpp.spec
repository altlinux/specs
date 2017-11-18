# BEGIN SourceDeps(oneline):
BuildRequires: perl(Authen/SASL.pm) perl(Net/Domain.pm) perl(Net/XMPP.pm) perl(open.pm) perl-devel
# END SourceDeps(oneline)
BuildRequires: /usr/bin/pod2man
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:	A Perl script to send XMPP messages
Name:		sendxmpp
Version:	1.24
Release:	alt1_5
License:	GPLv2
Group:		Communications
URL:		http://sendxmpp.hostname.sk/
Source:		https://github.com/lhost/%{name}/archive/v%{version}.tar.gz
BuildRequires:	rpm-build-perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildArch:	noarch
Source44: import.info

%description
Sendxmpp is a Perl script to send XMPP (Jabber) messages from the command
line, similar to what mail(1) does for mail. Messages can be sent both to
individual recipients and chat rooms.

%prep
%setup -q

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%files
%doc Changes README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
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
