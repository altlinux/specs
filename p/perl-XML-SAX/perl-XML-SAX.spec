%define dist XML-SAX
Name: perl-%dist
Version: 0.99
Release: alt1

Summary: Simple API for XML
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# default SAX driver
Requires: perl(XML/LibXML/SAX.pm)
# break dependency loop
Requires: perl-XML-LibXML

# Automatically added by buildreq on Thu Oct 06 2011
BuildRequires: perl-Encode perl-XML-NamespaceSupport perl-XML-SAX-Base perl-autodie perl-devel

%description
XML::SAX is a SAX parser access API for Perl. It includes classes
and APIs required for implementing SAX drivers, along with a factory
class for returning any SAX parser installed on the user's system.

%prep
%setup -q -n %dist-%version

# disable ParserDetails.ini update
sed -i- '/^sub MY::install/s/MY/notMY/' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

cat >%buildroot%perl_vendor_privlib/XML/SAX/ParserDetails.ini <<EOF
[XML::LibXML::SAX]
http://xml.org/sax/features/namespaces = 1
EOF

%files
%doc	README Changes
%dir	%perl_vendor_privlib/XML
%dir	%perl_vendor_privlib/XML/SAX
	%perl_vendor_privlib/XML/SAX.pm
	%perl_vendor_privlib/XML/SAX/*.pm
%doc	%perl_vendor_privlib/XML/SAX/*.pod
%exclude %perl_vendor_privlib/XML/SAX/PurePerl*
%config	%perl_vendor_privlib/XML/SAX/ParserDetails.ini

%changelog
* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 0.99-alt1
- 0.96 -> 0.99

* Mon Nov 15 2010 Vladimir Lettiev <crux@altlinux.ru> 0.96-alt2
- reverted previous changes (Closes: #24563)

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.96-alt1.1
- rebuilt with perl 5.12
- temporary break circular dependency on perl-XML-LibXML

* Tue Sep 16 2008 Alexey Tourbin <at@altlinux.ru> 0.96-alt1
- 0.16 -> 0.96

* Tue Mar 04 2008 Alexey Tourbin <at@altlinux.ru> 0.16-alt2
- changed default driver: XML::LibXML::SAX::Parser -> XML::LibXML::SAX

* Thu Jul 26 2007 Alexey Tourbin <at@altlinux.ru> 0.16-alt1
- 0.15 -> 0.16

* Tue Feb 27 2007 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- 0.14 -> 0.15

* Tue May 30 2006 Alexey Tourbin <at@altlinux.ru> 0.14-alt2
- got rid of /etc/perl5/XML/SAX/ParserDetails.ini
- XML::SAX::PurePerl not packaged

* Wed Apr 26 2006 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- 0.12 -> 0.14

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 0.12-alt5
- rebuild in new environment
- new subpackage: %name-PurePerl
- manual pages not packaged (use perldoc)

* Tue Aug 03 2004 Alexey Tourbin <at@altlinux.ru> 0.12-alt4
- removed %_sysconfdir/rpm/macros.d/%name
- removed triggers that register/unregister XML::SAX::PurePerl
- added dependency on XML::LibXML::SAX::Parser (the best parser backend)

* Wed Apr 28 2004 Alexey Tourbin <at@altlinux.ru> 0.12-alt3
- %_sysconfdir/rpm/macros.d/%name: regisger/unregister SAX API parsers
- added triggers that register/unregister XML::SAX::PurePerl

* Thu Sep 04 2003 Alexey Tourbin <at@altlinux.ru> 0.12-alt2
- buildreq re-applied (fixes build in the hasher)
- descriptions updated

* Fri Mar 21 2003 Stanislav Ievlev <inger@altlinux.ru> 0.12-alt1
- 0.12

* Tue Nov 12 2002 Stanislav Ievlev <inger@altlinux.ru> 0.11-alt1
- Initial release
