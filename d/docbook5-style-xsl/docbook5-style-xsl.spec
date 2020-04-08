Name: docbook5-style-xsl
Version: 1.79.2
Release: alt2
Group: Text tools

Summary: Norman Walsh's XSL stylesheets for DocBook 5.X

# Package is licensed as MIT/X (http://wiki.docbook.org/topic/DocBookLicense),
# some .js files under ./slides/browser/ are licensed MPLv1.1
License: MIT and MPL-1.1
Url: https://github.com/docbook/xslt10-stylesheets

Provides: docbook-xsl-ns = %version
# something that works
Requires: xml-common >= 0.6.3-alt15

BuildArch: noarch
Source0: https://github.com/docbook/xslt10-stylesheets/releases/download/release/%version/docbook-xsl-%version.tar

%description
These XSL namespace aware stylesheets allow you to transform any
DocBook 5 document to other formats, such as HTML, manpages, FO,
XHMTL and other formats. They are highly customizable. For more
information see W3C page about XSL.

%prep
%setup -n docbook-xsl-%version

%install
%global targetdir %_datadir/sgml/docbook/xsl-ns-stylesheets
mkdir -p %buildroot%targetdir-%version
cp -a [[:lower:]]* VERSION.xsl %buildroot%targetdir-%version/
ln -s VERSION.xsl %buildroot%targetdir-%version/VERSION
ln -s xsl-ns-stylesheets-%version %buildroot%targetdir

# Don't ship install shell script.
rm %buildroot%targetdir/install.sh
# Don't ship Java extensions in Fedora as they are not compiled from the source.
rm -r %buildroot%targetdir-%version/extensions

%add_findreq_skiplist %targetdir-%version/slides/slidy/help/help.html.* %targetdir-%version/epub/bin/dbtoepub

%post
for orig in 'http://cdn.docbook.org/release/xsl/%version' \
	   'http://cdn.docbook.org/release/xsl/current' \
	   'http://docbook.sourceforge.net/release/xsl-ns/current'; do
	for type in rewriteSystem rewriteURI; do
		xmlcatalog --noout --add "$type" \
		"$orig" 'file://%targetdir-%version' \
		%_sysconfdir/xml/catalog
	done
done

%postun
if [ "$1" = 0 ]; then
	xmlcatalog --noout --del \
		'file://%targetdir-%version' \
		%_sysconfdir/xml/catalog
fi

%files
%targetdir/
%targetdir-%version/
%doc README COPYING RELEASE-NOTES.txt NEWS BUGS

%changelog
* Thu Apr 09 2020 Dmitry V. Levin <ldv@altlinux.org> 1.79.2-alt2
- Cleaned up.
- Forcibly removed ruby dependencies.

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.79.2-alt1_4
- update to new release by fcimport

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

