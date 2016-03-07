# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(threads.pm) perl(threads/shared.pm) perl-pod perl-podlators perldoc
# END SourceDeps(oneline)
Name:           perl-Net-Jabber
Version:        2.0
Release:        alt3_28
Summary:        Net::Jabber - Jabber Perl Library
Group:          Development/Perl
License:        (GPL+ or Artistic) or LGPLv2+
URL:            http://search.cpan.org/dist/Net-Jabber/
Source0: http://search.cpan.org/CPAN/authors/id/R/RE/REATMON/Net-Jabber-%{version}.tar.gz
Source1:        LICENSING.correspondance
Patch0:         Net-Jabber-2.0-timezone.patch
BuildArch:      noarch
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Net/XMPP.pm)
BuildRequires:  perl(Net/XMPP/Client.pm)
BuildRequires:  perl(Net/XMPP/Connection.pm)
BuildRequires:  perl(Net/XMPP/Debug.pm)
BuildRequires:  perl(Net/XMPP/IQ.pm)
BuildRequires:  perl(Net/XMPP/JID.pm)
BuildRequires:  perl(Net/XMPP/Message.pm)
BuildRequires:  perl(Net/XMPP/Namespaces.pm)
BuildRequires:  perl(Net/XMPP/Presence.pm)
BuildRequires:  perl(Net/XMPP/Stanza.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Time/Timezone.pm)
# file requires for prep
BuildRequires:  %{_bindir}/perldoc
Requires:  perl(Time/Timezone.pm)
Source44: import.info

%description
Net::Jabber provides a Perl user with access to the Jabber Instant
Messaging protocol.

For more information about Jabber visit:

    http://www.jabber.org

%prep
%setup -q -n Net-Jabber-%{version}
%patch0 -p1
cp %{SOURCE1} .
# generate our other two licenses...
perldoc perlgpl > LICENSE.GPL
perldoc perlartistic > LICENSE.Artistic
# we really don't want executable examples...
chmod -x examples/*

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*
# fix wonky execute permissions
find %{buildroot} -type f -exec chmod -x '{}' ';'

%check
# Disable tests which will fail under mock
rm t/protocol_definenamespace.t
rm t/protocol_muc.t
rm t/protocol_rpc.t
make test

%files
%doc CHANGES README examples LICENSE.* LICENSING.*
%{perl_vendor_privlib}/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_28
- update to new release by fcimport

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_27
- replaced by imported version

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 2.0-alt3
- added dependency on perl-Time-modules

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 2.0-alt2
- rebuilt

* Wed Mar 16 2005 Alexey Tourbin <at@altlinux.ru> 2.0-alt1
- 1.30 -> 2.0
- build against system Test::More (removed t/lib/Test)
- manual pages not packaged (use perldoc)

* Fri Apr 16 2004 Alexey Tourbin <at@altlinux.ru> 1.30-alt1
- 1.29 -> 1.30

* Tue Oct 28 2003 Alexey Tourbin <at@altlinux.ru> 1.29-alt1
- initial revision
