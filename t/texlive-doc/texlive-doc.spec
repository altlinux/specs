Name: texlive-doc
Version: 2008.0
Release: alt0.10
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: TeX Live documentation
License: Distributable
Group: Publishing
Url: http://tug.org/texlive/

Source0: %name-texmf-%version-%release.tar
Source1: %name-texmf-doc-%version-%release.tar
Source2: %name-alt-%version.tar

BuildArch: noarch

BuildRequires: tex-common texlive-common
BuildRequires: perl-SGMLSpm
BuildRequires: less vim-console rpm-utils automake autoconf

Requires: texlive-base-bin, texlive-doc-base

%set_compress_method none

# don't check documentation and sources
%add_findreq_skiplist %_datadir/texmf/doc/*
%add_findreq_skiplist %_datadir/texmf-texlive/doc/*
%add_findreq_skiplist %_datadir/texmf/source/*
%add_findreq_skiplist %_datadir/texmf-texlive/source/*

%description
TeX Live documentation

%package -n texlive-doc-base
Group: Publishing
Summary: TeX Live documentation

%description -n texlive-doc-base
(none)

%package -n texlive-doc-bg
Group: Publishing
Summary: Bulgarian documentation
Requires: texlive-doc-base

%description -n texlive-doc-bg
(none)

%package -n texlive-doc-zh
Group: Publishing
Summary: Chinese documentation
Requires: texlive-doc-base

%description -n texlive-doc-zh
(none)

%package -n texlive-doc-cs+sk
Group: Publishing
Summary: Czechslovak documentation
Requires: texlive-doc-base

%description -n texlive-doc-cs+sk
(none)

%package -n texlive-doc-nl
Group: Publishing
Summary: Dutch documentation
Requires: texlive-doc-base

%description -n texlive-doc-nl
(none)

%package -n texlive-doc-en
Group: Publishing
Summary: English documentation
Requires: texlive-doc-base
# file conflicts
Conflicts: tetex-core

%description -n texlive-doc-en
(none)

%package -n texlive-doc-fi
Group: Publishing
Summary: Finnish documentation
Requires: texlive-doc-base

%description -n texlive-doc-fi
(none)

%package -n texlive-doc-fr
Group: Publishing
Summary: French documentation
Requires: texlive-doc-base

%description -n texlive-doc-fr
(none)

%package -n texlive-doc-de
Group: Publishing
Summary: German documentation
Requires: texlive-doc-base

%description -n texlive-doc-de
(none)

%package -n texlive-doc-el
Group: Publishing
Summary: Greek documentation
Requires: texlive-doc-base

%description -n texlive-doc-el
(none)

%package -n texlive-doc-it
Group: Publishing
Summary: Italian documentation
Requires: texlive-doc-base

%description -n texlive-doc-it
(none)

%package -n texlive-doc-ja
Group: Publishing
Summary: Japanese documentation
Requires: texlive-doc-base

%description -n texlive-doc-ja
(none)

%package -n texlive-doc-ko
Group: Publishing
Summary: Korean documentation
Requires: texlive-doc-base

%description -n texlive-doc-ko
(none)

%package -n texlive-doc-mn
Group: Publishing
Summary: Mongolian documentation
Requires: texlive-doc-base

%description -n texlive-doc-mn
(none)

%package -n texlive-doc-pl
Group: Publishing
Summary: Polish documentation
Requires: texlive-doc-base

%description -n texlive-doc-pl
(none)

%package -n texlive-doc-pt
Group: Publishing
Summary: Portuguese documentation
Requires: texlive-doc-base

%description -n texlive-doc-pt
(none)

%package -n texlive-doc-ru
Group: Publishing
Summary: Russian documentation
Requires: texlive-doc-base

%description -n texlive-doc-ru
(none)

%package -n texlive-doc-sl
Group: Publishing
Summary: Slovenian documentation
Requires: texlive-doc-base

%description -n texlive-doc-sl
(none)

%package -n texlive-doc-es
Group: Publishing
Summary: Spanish documentation
Requires: texlive-doc-base

%description -n texlive-doc-es
(none)

%package -n texlive-doc-th
Group: Publishing
Summary: Thai documentation
Requires: texlive-doc-base

%description -n texlive-doc-th
(none)

%package -n texlive-doc-tr
Group: Publishing
Summary: Turkish documentation
Requires: texlive-doc-base

%description -n texlive-doc-tr
(none)

%package -n texlive-doc-uk
Group: Publishing
Summary: Ukrainian documentation
Requires: texlive-doc-base

%description -n texlive-doc-uk
(none)

%package -n texlive-doc-vi
Group: Publishing
Summary: Vietnamese documentation
Requires: texlive-doc-base

%description -n texlive-doc-vi
(none)

%prep
%setup -c -T -a2

%install
mkdir -p %buildroot/%_datadir
tar xf %SOURCE0 -C %buildroot/%_datadir/
tar xf %SOURCE1 -C %buildroot/%_datadir/

mkdir -p %buildroot/%_datadir/texmf/doc
cd %buildroot/%_datadir/texmf-doc/
tar cf - . | tar xf - -C %buildroot/%_datadir/texmf/

%files -n texlive-doc-base -f alt-linux/texlive-doc-base.files

%files -n texlive-doc-bg -f alt-linux/texlive-doc-bg.files

%files -n texlive-doc-zh -f alt-linux/texlive-doc-zh.files

%files -n texlive-doc-cs+sk -f alt-linux/texlive-doc-cs+sk.files

%files -n texlive-doc-nl -f alt-linux/texlive-doc-nl.files

%files -n texlive-doc-en -f alt-linux/texlive-doc-en.files

%files -n texlive-doc-fi -f alt-linux/texlive-doc-fi.files

%files -n texlive-doc-fr -f alt-linux/texlive-doc-fr.files

%files -n texlive-doc-de -f alt-linux/texlive-doc-de.files

%files -n texlive-doc-el -f alt-linux/texlive-doc-el.files

%files -n texlive-doc-it -f alt-linux/texlive-doc-it.files

%files -n texlive-doc-ja -f alt-linux/texlive-doc-ja.files

%files -n texlive-doc-ko -f alt-linux/texlive-doc-ko.files

%files -n texlive-doc-mn -f alt-linux/texlive-doc-mn.files

%files -n texlive-doc-pl -f alt-linux/texlive-doc-pl.files

%files -n texlive-doc-pt -f alt-linux/texlive-doc-pt.files

%files -n texlive-doc-ru -f alt-linux/texlive-doc-ru.files

%files -n texlive-doc-sl -f alt-linux/texlive-doc-sl.files

%files -n texlive-doc-es -f alt-linux/texlive-doc-es.files

%files -n texlive-doc-th -f alt-linux/texlive-doc-th.files

%files -n texlive-doc-tr -f alt-linux/texlive-doc-tr.files

%files -n texlive-doc-uk -f alt-linux/texlive-doc-uk.files

%files -n texlive-doc-vi -f alt-linux/texlive-doc-vi.files

%changelog
* Thu Mar 26 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.10
- Re-arrange documentation
  + leave texmf/doc and texmf-texlive/doc untouched
  + move man1 and man5 pages to %%_mandir

* Thu Feb 26 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.9
- Add tex-common and texlive-common to BuildRequires.
- Set conflicts with tetex-* packages.

* Tue Feb 17 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.7
- Slovenian documentation was added.

* Fri Oct 31 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.4
- Sources repacked.

* Wed Oct 08 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.1
- Initial build for ALT Linux.
