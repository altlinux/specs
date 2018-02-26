%define pear_name XML_HTMLSax3

Name: pear-XML_HTMLSax3
Version: 3.0.0
Release: alt3

Summary: A SAX parser for HTML and other badly formed XML documents

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/XML_HTMLSax3

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_HTMLSax3-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
XML_HTMLSax3 is a SAX based XML parser for badly formed XML documents, such
as HTML.
  The original code base was developed by Alexander Zhukov and published
at http://sourceforge.net/projects/phpshelve/. Alexander kindly gave
permission to modify the code and license for inclusion in PEAR.

  NOTE!
  This package is now dual licensed under PHP license v3.01 and LGPL 3.0
  See the CVS repo link for the actual licenses

  PEAR::XML_HTMLSax3 provides an API very similar to the native PHP XML
extension (http://www.php.net/xml), allowing handlers using one to be
easily adapted to the other. The key difference is HTMLSax will not break
on badly formed XML, allowing it to be used for parsing HTML documents.
Otherwise HTMLSax supports all the handlers available from Expat except
namespace and external entity handlers. Provides methods for handling XML
escapes as well as JSP/ASP opening and close tags.

  Version 1.x introduced an API similar to the native SAX extension but
used a slow character by character approach to parsing.

  Version 2.x has had it's internals completely overhauled to use a Lexer,
delivering performance *approaching* that of the native XML extension, as
well as a radically improved, modular design that makes adding further
functionality easy.

  Version 3.x is about fine tuning the API, behaviour and providing a
mechanism to distinguish HTML "quirks" from badly formed HTML (later
functionality not yet implemented)

  A big thanks to Jeff Moore (lead developer of WACT:
http://wact.sourceforge.net) who's largely responsible for new design, as
well input from other members at Sitepoint's Advanced PHP forums:
http://www.sitepointforums.com/showthread.php?threadid=121246.

  Thanks also to Marcus Baker (lead developer of SimpleTest:
http://www.lastcraft.com/simple_test.php) for sorting out the unit tests.

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/XML
%pear_testdir/XML_HTMLSax3/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- initial build for ALT Linux Sisyphus

