%define cid            langpack-be@firefox.mozilla.org
%define cid_dir        %firefox_noarch_extensionsdir/%cid

%define cid_dict       be@dictionaries.addons.mozilla.org
%define cid_dict_dir   %firefox_noarch_extensionsdir/%cid_dict

Name:		firefox-be
Version:	50.0
Release:	alt1
Summary:	Belarusian (BE) Language Pack for Firefox

License:	GPL
Group:		Networking/WWW
URL:		http://mozilla-be.sourceforge.net

Source0:	be.xpi

Requires:	hunspell-be

BuildRequires(pre):	rpm-build-firefox
BuildRequires:		unzip

BuildArch: 		noarch

Packager:	Alexey Gladkov <legion@altlinux.ru>

%description
The Mozilla Firefox Belarusian translation.

%prep
%setup -c -n %name-%version/%cid

%install
cd ..

mkdir -p -- \
	%buildroot/%cid_dir \
	%buildroot/%cid_dict_dir/dictionaries

# Install translation
cp -r -- %cid/* %buildroot/%cid_dir

# Install dictionary
cat > %buildroot/%cid_dict_dir/install.rdf <<-EOF
	<?xml version="1.0"?>
	<RDF xmlns="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	     xmlns:em="http://www.mozilla.org/2004/em-rdf#">
	  <Description about="urn:mozilla:install-manifest"
	               em:id="%cid_dict"
	               em:name="Belarusian (BE) Dictionary"
	               em:version="%version"
	               em:type="64"
	               em:unpack="true"
	               em:creator="Mozilla Russia">
	    <em:targetApplication>
	      <Description>
	        <em:id>{ec8030f7-c20a-464f-9b0e-13a3a9e97384}</em:id>
	        <em:minVersion>%version</em:minVersion>
	        <em:maxVersion>%version.*</em:maxVersion>
	      </Description>
	    </em:targetApplication>
	  </Description>
	</RDF>
EOF
ln -s %_datadir/myspell/be_BY.aff %buildroot/%cid_dict_dir/dictionaries/be.aff
ln -s %_datadir/myspell/be_BY.dic %buildroot/%cid_dict_dir/dictionaries/be.dic

%files
%cid_dir
%cid_dict_dir

%changelog
* Thu Nov 17 2016 Alexey Gladkov <legion@altlinux.ru> 50.0-alt1
- New version (50.0).

* Thu Sep 29 2016 Alexey Gladkov <legion@altlinux.ru> 49.0.1-alt1
- New version (49.0.1).

* Wed Aug 10 2016 Alexey Gladkov <legion@altlinux.ru> 48.0-alt1
- New version (48.0).

* Tue Jun 21 2016 Alexey Gladkov <legion@altlinux.ru> 47.0-alt1
- New version (47.0).

* Sun May 01 2016 Alexey Gladkov <legion@altlinux.ru> 46.0-alt1
- New version (46.0).

* Tue Mar 22 2016 Alexey Gladkov <legion@altlinux.ru> 45.0.1-alt1
- New version (45.0.1).

* Thu Jan 28 2016 Alexey Gladkov <legion@altlinux.ru> 44.0-alt1
- New version (44.0).

* Thu Dec 24 2015 Alexey Gladkov <legion@altlinux.ru> 43.0.1-alt1
- New version (43.0.1).

* Tue Nov 10 2015 Alexey Gladkov <legion@altlinux.ru> 42.0-alt1
- New version (42.0).

* Tue Sep 29 2015 Alexey Gladkov <legion@altlinux.ru> 41.0-alt1
- New version (41.0).

* Mon Aug 17 2015 Alexey Gladkov <legion@altlinux.ru> 40.0.2-alt1
- New version (40.0.2).

* Mon Aug 10 2015 Alexey Gladkov <legion@altlinux.ru> 39.0.3-alt1
- New version (39.0.3).

* Mon May 25 2015 Alexey Gladkov <legion@altlinux.ru> 38.0.1-alt1
- New version (38.0.1).

* Thu Apr 09 2015 Alexey Gladkov <legion@altlinux.ru> 37.0.1-alt1
- New version (37.0.1).

* Mon Mar 09 2015 Alexey Gladkov <legion@altlinux.ru> 36.0.1-alt1
- New version (36.0.1).

* Tue Jan 27 2015 Alexey Gladkov <legion@altlinux.ru> 35.0-alt1
- New version (35.0).

* Mon Dec 08 2014 Alexey Gladkov <legion@altlinux.ru> 34.0-alt1
- New version (34.0).

* Fri Oct 24 2014 Alexey Gladkov <legion@altlinux.ru> 33.0-alt1
- New version (33.0).

* Wed Oct 01 2014 Alexey Gladkov <legion@altlinux.ru> 32.0-alt1
- New version (32.0).

* Wed Jul 30 2014 Alexey Gladkov <legion@altlinux.ru> 31.0-alt1
- New version (31.0).

* Sun May 11 2014 Alexey Gladkov <legion@altlinux.ru> 29.0.1-alt1
- New version (29.0.1).

* Thu Mar 27 2014 Alexey Gladkov <legion@altlinux.ru> 28.0-alt1
- New version (28.0).

* Fri Feb 14 2014 Alexey Gladkov <legion@altlinux.ru> 27.0-alt1
- New version (27.0).

* Sat Dec 28 2013 Alexey Gladkov <legion@altlinux.ru> 26.0-alt1
- New version (26.0).

* Wed Nov 06 2013 Alexey Gladkov <legion@altlinux.ru> 25.0-alt1
- New version (25.0).

* Fri Oct 25 2013 Alexey Gladkov <legion@altlinux.ru> 24.0-alt1
- New version (24.0).

* Wed Aug 14 2013 Alexey Gladkov <legion@altlinux.ru> 23.0-alt1
- New version (23.0).

* Mon Jul 01 2013 Alexey Gladkov <legion@altlinux.ru> 22.0-alt1
- New version (22.0).

* Tue Jun 18 2013 Alexey Gladkov <legion@altlinux.ru> 21.0-alt2
- Add dictionary extension (ALT#29063).

* Wed Jun 05 2013 Alexey Gladkov <legion@altlinux.ru> 21.0-alt1
- New version (21.0).

* Mon Apr 15 2013 Alexey Gladkov <legion@altlinux.ru> 20.0-alt1
- New version (20.0).

* Wed Mar 06 2013 Alexey Gladkov <legion@altlinux.ru> 19.0.1-alt1
- New version (19.0.1).

* Fri Jan 18 2013 Alexey Gladkov <legion@altlinux.ru> 18.0-alt1
- New version (18.0).

* Sat Nov 24 2012 Alexey Gladkov <legion@altlinux.ru> 17.0-alt1
- New version (17.0).

* Mon Oct 29 2012 Alexey Gladkov <legion@altlinux.ru> 16.0.1-alt1
- New version (16.0.1).

* Sun Sep 02 2012 Alexey Gladkov <legion@altlinux.ru> 15.0-alt1
- New version (15.0).

* Sun Aug 05 2012 Alexey Gladkov <legion@altlinux.ru> 14.0.1-alt1
- New version (14.0.1).

* Tue Jul 10 2012 Alexey Gladkov <legion@altlinux.ru> 13.0.1-alt1
- New version (13.0.1).

* Tue May 08 2012 Alexey Gladkov <legion@altlinux.ru> 12.0-alt1
- New version (12.0).

* Wed Apr 25 2012 Alexey Gladkov <legion@altlinux.ru> 11.0-alt1
- New version (11.0).

* Sun Feb 26 2012 Alexey Gladkov <legion@altlinux.ru> 10.0.2-alt1
- New version (10.0.2).

* Wed Jan 18 2012 Alexey Gladkov <legion@altlinux.ru> 9.0.1-alt1
- New version (9.0.1).

* Mon Nov 21 2011 Alexey Gladkov <legion@altlinux.ru> 8.0-alt1
- New version (8.0).

* Wed Oct 12 2011 Alexey Gladkov <legion@altlinux.ru> 7.0.1-alt1
- New version (7.0.1).

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.2-alt1
- New version (6.0.2).

* Fri Aug 26 2011 Alexey Gladkov <legion@altlinux.ru> 6.0-alt1
- New version (6.0).

* Mon Aug 01 2011 Alexey Gladkov <legion@altlinux.ru> 5.0.1-alt1
- New version (5.0.1).

* Tue May 03 2011 Alexey Gladkov <legion@altlinux.ru> 4.0.1-alt1
- New version (4.0.1).

* Mon Apr 18 2011 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt2
- Remove bundled dictionary, use system hunspell.

* Mon Apr 18 2011 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt1.1
- fix typo in buildreq.

* Mon Apr 18 2011 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt1
- Rebuild for fx4. Consolidate translation with spellcheck dictionary
  like -ru version.

* Sun Mar 18 2007 L.A. Kostis <lakostis@altlinux.ru> 2.0-alt2
- fix extensions dir.
- use unzip instead internal rpm commands.

* Sun Nov 26 2006 L.A. Kostis <lakostis@altlinux.ru> 2.0-alt1
- new version for Firefox 2.0.
- remove obsoleted macros.

* Wed Sep 27 2006 L.A. Kostis <lakostis@altlinux.ru> 1.5.0.7-alt1
- rebuild for Firefox 1.5.0.7.

* Thu Aug 10 2006 L.A. Kostis <lakostis@altlinux.ru> 1.5.0.6-alt1
- rebuild for Firefox 1.5.0.6.
- prepare for gear.

* Thu Jun 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.4-alt1
- rebuild with firefox 1.5.0.4

* Mon May 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.3-alt1
- made from 20060312 translation snapshot.
- rebuild with firefox 1.5.0.3

* Sun Dec 25 2005 LAKostis <lakostis at altlinux.ru> 1.5-alt1
- made from 20051217 translation snapshot.
- rebuild with new firefox.
- update .spec for new build scheme.

* Thu Nov 10 2005 Konstantin A Lepikhov (L.A. Kostis) <lakostis@altlinux.ru> 1.0.7-alt1.5
- rebuild with new firefox.

* Thu Oct 13 2005 Konstantin A Lepikhov (L.A. Kostis) <lakostis@altlinux.ru> 1.0.7-alt1.4
- rebuild with new firefox.

* Fri Aug 26 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1.3
- firefox after firefox-ru installation will be switched to be_BY.
- postun script bugfix.

* Tue Aug 16 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1.1.2
- bugfix rebuild.

* Mon Aug 15 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1.1.1
- Rebuild with new firefox.

* Tue Jul 12 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt1.1
- fix URL.

* Tue Jul 05 2005 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- rebuilt for Sisyphus, lakostis' package

* Wed Jul 05 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt0
- made from 20050119 translation snapshot.
- First build for ALT Linux.
