%define ciddir	%tbird_noarch_extensionsdir/langpack-ru@thunderbird.mozilla.org

Name:		thunderbird-ru
Version:	13.0.1
Release:	alt1
Summary:	Russian (RU) Language Pack for Thunderbird

License:	GPL
Group:		Networking/Mail
URL:		http://www.mozilla-russia.org/products/thunderbird/
Packager:	Alexey Gladkov <legion@altlinux.ru>
BuildArch:	noarch

Source0:	ru-%version.xpi

Requires:	hunspell-ru

BuildRequires(pre):	rpm-build-thunderbird 
BuildRequires:		unzip

%description
The Mozilla Thunderbird in Russian.

%install
%__mkdir_p %buildroot/%ciddir
unzip -qq -d %buildroot/%ciddir %SOURCE0

rm -rf -- %buildroot/%ciddir/dictionaries
%__mkdir_p %buildroot/%ciddir/dictionaries

(set +x
	for suf in aff dic; do
		t="$(relative %_datadir/myspell/ru_RU.$suf %ciddir/dictionaries/)"
		ln -vs "$t" %buildroot/%ciddir/dictionaries/ru.$suf
	done
)

%files
%ciddir

%changelog
* Tue Jul 10 2012 Alexey Gladkov <legion@altlinux.ru> 13.0.1-alt1
- New version (13.0.1).

* Thu May 10 2012 Alexey Gladkov <legion@altlinux.ru> 12.0.1-alt1
- new version (12.0.1).

* Wed Apr 25 2012 Alexey Gladkov <legion@altlinux.ru> 11.0.1-alt1
- new version (11.0.1).

* Wed Apr 25 2012 Alexey Gladkov <legion@altlinux.ru> 11.0-alt1
- new version (11.0).

* Sun Feb 26 2012 Alexey Gladkov <legion@altlinux.ru> 10.0.2-alt1
- new version (10.0.2).

* Mon Nov 21 2011 Alexey Gladkov <legion@altlinux.ru> 8.0-alt1
- new version (8.0).

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.1-alt1
- new version (6.0.1).

* Fri Aug 26 2011 Alexey Gladkov <legion@altlinux.ru> 6.0-alt1
- new version (6.0).

* Tue Aug 02 2011 Alexey Gladkov <legion@altlinux.ru> 5.0-alt1
- new version (5.0).

* Mon Aug 16 2010 Alexey Gladkov <legion@altlinux.ru> 3.1.2-alt1
- new version (3.1.2).

* Tue Apr 06 2010 Alexey Gladkov <legion@altlinux.ru> 3.0.4-alt1
- new version (3.0.4).

* Sat Jan 30 2010 Alexey Gladkov <legion@altlinux.ru> 3.0.1-alt1
- new version (3.0.1).

* Sun Oct 18 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt5
- new shapshot (3.0 20091018).

* Tue Sep 29 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt4
- new shapshot (3.0 20090929).

* Mon Aug 17 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt3
- new shapshot (3.0 20090917).

* Wed Jun 03 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt2
- new shapshot (3.0 20090603).

* Thu Mar 12 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1
- new shapshot (3.0 20090312).

* Mon Jul 02 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.0-alt2
- Rebuild with new thunderbird (2.0.0.4).

* Mon Apr 23 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.0-alt1
- new version (2.0.0.0).

* Sun Mar 11 2007 Alexey Gladkov <legion@altlinux.ru> 2.0-alt1
- new version (2.0).
- remove noarch.
- rename dictionaries.

* Thu Nov 23 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.8-alt1
- Rebuild with new thunderbird (1.5.0.8).

* Fri Sep 08 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.5-alt3
- Update install.rdf.

* Mon Sep 04 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.5-alt2
- Remove SOURCE1 (fix #9556).

* Mon Aug 21 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.5-alt1
- Rebuild with thunderbird-1.5.0.5-alt1.

* Tue May 02 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.2-alt1
- new version.

* Thu Mar 23 2006 Alexey Gladkov <legion@altlinux.ru> 1.5-alt1
- new version.

* Wed Aug 24 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt2
- packaging bugfix.

* Mon Aug 15 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1
- new version;

* Thu May 12 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.2-alt1
- new version;

* Thu Jan 20 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2
- Rebuild with new thunderbird.
- Requires to thunderbird package was relaxed.

* Sat Jan 08 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- new version;

* Tue Dec 30 2003 Alexey Gladkov <legion@altlinux.ru> 0.4-alt2
- First build for ALT Linux.
