%add_findreq_skiplist %_datadir/sgml/docbook/xsl-ns-stylesheets-*/slides/slidy/help/help.html.*
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: docbook5-style-xsl
Version: 1.79.2
Release: alt1_3
Group: Text tools

Summary: Norman Walsh's XSL stylesheets for DocBook 5.X

# Package is licensed as MIT/X (http://wiki.docbook.org/topic/DocBookLicense),
# some .js files under ./slides/browser/ are licensed MPLv1.1
License: MIT and MPLv1.1
URL: https://github.com/docbook/xslt10-stylesheets

Provides: docbook-xsl-ns = %{version}
# xml-common was using /usr/share/xml until 0.6.3-8.
Requires: xml-common >= 0.6.3
# libxml2 required because of usage of /usr/bin/xmlcatalog
Requires(post): libxml2 xml-utils
Requires(postun): libxml2 xml-utils
Conflicts: passivetex < 1.21

BuildArch: noarch
Source0: https://github.com/docbook/xslt10-stylesheets/releases/download/release%2F{%version}/docbook-xsl-%{version}.tar.bz2

%description
These XSL namespace aware stylesheets allow you to transform any
DocBook 5 document to other formats, such as HTML, manpages, FO,
XHMTL and other formats. They are highly customizable. For more
information see W3C page about XSL.

#Don't ship Java extensions in Fedora as they are not compiled from the source
#Shiping sources instead of binary jars was requested by
#https://lists.oasis-open.org/archives/docbook-apps/201408/msg00008.html
#Sources available in the docbook stylesheets svn repository, but not packaged.
%if 0%{?rhel} >= 7
%package extensions
Group: Text tools
Summary: Norman Walsh's XSL stylesheets extensions for DocBook 5.X
# Package is licensed as MIT/X (http://wiki.docbook.org/topic/DocBookLicense),
# some .js files under ./slides/browser/ are licensed MPLv1.1
License: MIT and ASL 2.0
Requires: docbook-xsl-ns = %{version}

%description extensions
This package contains Java extensions for XSL namespace aware stylesheets.
%endif

%prep
%setup -q -n docbook-xsl-%{version}
#remove .gitignore files
rm -rf $(find -name '.gitignore' -type f)
#make ruby scripts executable
chmod +x epub/bin/dbtoepub

%build

%install
DESTDIR=$RPM_BUILD_ROOT
mkdir -p $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%version
cp -a [[:lower:]]* $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%version/
cp -a VERSION $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%version/VERSION.xsl
ln -s VERSION.xsl \
$DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%version/VERSION
ln -s xsl-ns-stylesheets-%{version} \
 $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets

# Don't ship install shell script.
rm -rf $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets/install.sh

%files
%doc BUGS
%doc README COPYING
%doc TODO NEWS
%doc RELEASE-NOTES.*
%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}
%{_datadir}/sgml/docbook/xsl-ns-stylesheets
%exclude %{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}/extensions

%if 0%{?rhel} >= 7
%files extensions
%doc extensions/README.txt extensions/LICENSE.txt
%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}/extensions
%endif

%post
CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://cdn.docbook.org/release/xsl/%{version}" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://cdn.docbook.org/release/xsl/%{version}" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://cdn.docbook.org/release/xsl/current/" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://cdn.docbook.org/release/xsl/current/" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG

%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://docbook.sourceforge.net/release/xsl-ns/current" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://docbook.sourceforge.net/release/xsl-ns/current" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG

%postun
if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
   "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
fi

%changelog
* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.79.2-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.78.1-alt1_7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.78.1-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.78.1-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.78.1-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.78.1-alt1_2
- update to new release by fcimport

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.78.1-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.78.0-alt1_3
- update to new release by fcimport

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.78.0-alt1_2
- fc update

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.78.0-alt1_1
- update to new release by fcimport

* Wed Oct 24 2012 Fr. Br. George <george@altlinux.ru> 1.77.1-alt1_2.1
- Provide VERSION.xsl, which included from source

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.77.1-alt1_2
- new version

* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 1.76.0-alt1_1
- converted from Fedora by srpmconvert script

