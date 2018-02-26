Name: svn2cl
Version: 0.11
Release: alt1
Summary: Create a ChangeLog from a Subversion log

Group: Development/Tools
License: BSD
Url: http://ch.tudelft.nl/~arthur/svn2cl/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://ch.tudelft.nl/~arthur/svn2cl/%name-%version.tar.gz

BuildArch: noarch

%description
svn2cl is a simple xsl transformation and shellscript wrapper for
generating a classic GNU-style ChangeLog from a subversion repository
log.  It is made from several changelog-like scripts using common xslt
constructs found in different places.

%prep
%setup
%__subst 's|^XSL="$dir/|XSL="%_datadir/svn2cl/|' svn2cl.sh

%build
%install
install -Dpm 755 svn2cl.sh %buildroot%_bindir/svn2cl

install -dm 755 %buildroot%_datadir/svn2cl
install -pm 644 *.xsl %buildroot%_datadir/svn2cl

install -Dpm 644 svn2cl.1 %buildroot%_man1dir/svn2cl.1

%files
%doc ChangeLog NEWS README TODO authors.xml svn2html.css
%_bindir/svn2cl
%_datadir/svn2cl/
%_man1dir/svn2cl.1*

%changelog
* Sat Sep 19 2009 Boris Savelev <boris@altlinux.org> 0.11-alt1
- initial build for Sisyphus

* Sun Dec 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.11-1
- 0.11.

* Sun Apr  6 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.10-1
- 0.10, drop disttag.

* Sun Apr  8 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.9-1
- 0.9.

* Thu Oct 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.8-1
- 0.8.
- Add (empty) %%build section.

* Fri Sep 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7-2
- Rebuild.

* Fri Jun  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7-1
- 0.7.

* Fri Apr  7 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.6-1
- First FE build (#186632).

* Thu Mar 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.6-0.1
- First build.
