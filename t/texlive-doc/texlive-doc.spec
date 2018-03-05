# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

%define enable_asymptote	0
%define enable_xindy		1

%define with_system_dialog	1
%define with_system_lcdf	0
%define with_system_poppler	0
%define with_system_psutils	1
%define with_system_t1lib	1
%define with_system_tex4ht	0
%define with_system_teckit	0

%define texmfbindir		%{_bindir}
%define texmfdir		%{_datadir}/texmf
%define texmfdistdir		%{_datadir}/texmf-dist
%define texmflocaldir		%{_datadir}/texmf-local
%define texmfextradir		%{_datadir}/texmf-extra
%define texmffontsdir		%{_datadir}/texmf-fonts
%define texmfprojectdir	%{_datadir}/texmf-project
%define texmfvardir		%{_localstatedir}/lib/texmf
%define texmfconfdir		%{_sysconfdir}/texmf

%define relYear 2017
%global tl_version %relYear
%global mga_tl_timestamp 20170524

Name:		texlive-doc
Version:	%relYear
Release:	alt2_2
#Summary:	The TeX formatting system
#Group:		Publishing
License:	http://www.tug.org/texlive/LICENSE.TL
URL:		http://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/%{relYear}/texlive-%{mga_tl_timestamp}-texmf-doc.tar.xz

BuildArch:	noarch
AutoReqProv: no

#-----------------------------------------------------------------------
#add_cleanup_skiplist for safety if cleanup is enabled
%set_cleanup_method none
%add_cleanup_skiplist %{texmfdistdir}/doc/fonts/cmcyr/coding.bak

#-----------------------------------------------------------------------


#package	-n texlive-doc
Summary:	Tex Live documentation
Group:		Documentation
Requires:	texlive-texmf = %{version}
Provides: texlive-doc-base = %{tl_version}
Conflicts: texlive-doc-base < 2009
Obsoletes: texlive-doc-base < 2009
Provides: texlive-doc-bg = %{tl_version}
Conflicts: texlive-doc-bg < 2009
Obsoletes: texlive-doc-bg < 2009
Provides: texlive-doc-cs+sk = %{tl_version}
Conflicts: texlive-doc-cs+sk < 2009
Obsoletes: texlive-doc-cs+sk < 2009
Provides: texlive-doc-de = %{tl_version}
Conflicts: texlive-doc-de < 2009
Obsoletes: texlive-doc-de < 2009
Provides: texlive-doc-el = %{tl_version}
Conflicts: texlive-doc-el < 2009
Obsoletes: texlive-doc-el < 2009
Provides: texlive-doc-en = %{tl_version}
Conflicts: texlive-doc-en < 2009
Obsoletes: texlive-doc-en < 2009
Provides: texlive-doc-es = %{tl_version}
Conflicts: texlive-doc-es < 2009
Obsoletes: texlive-doc-es < 2009
Provides: texlive-doc-fi = %{tl_version}
Conflicts: texlive-doc-fi < 2009
Obsoletes: texlive-doc-fi < 2009
Provides: texlive-doc-fr = %{tl_version}
Conflicts: texlive-doc-fr < 2009
Obsoletes: texlive-doc-fr < 2009
Provides: texlive-doc-it = %{tl_version}
Conflicts: texlive-doc-it < 2009
Obsoletes: texlive-doc-it < 2009
Provides: texlive-doc-ja = %{tl_version}
Conflicts: texlive-doc-ja < 2009
Obsoletes: texlive-doc-ja < 2009
Provides: texlive-doc-ko = %{tl_version}
Conflicts: texlive-doc-ko < 2009
Obsoletes: texlive-doc-ko < 2009
Provides: texlive-doc-mn = %{tl_version}
Conflicts: texlive-doc-mn < 2009
Obsoletes: texlive-doc-mn < 2009
Provides: texlive-doc-nl = %{tl_version}
Conflicts: texlive-doc-nl < 2009
Obsoletes: texlive-doc-nl < 2009
Provides: texlive-doc-pl = %{tl_version}
Conflicts: texlive-doc-pl < 2009
Obsoletes: texlive-doc-pl < 2009
Provides: texlive-doc-pt = %{tl_version}
Conflicts: texlive-doc-pt < 2009
Obsoletes: texlive-doc-pt < 2009
Provides: texlive-doc-ru = %{tl_version}
Conflicts: texlive-doc-ru < 2009
Obsoletes: texlive-doc-ru < 2009
Provides: texlive-doc-sl = %{tl_version}
Conflicts: texlive-doc-sl < 2009
Obsoletes: texlive-doc-sl < 2009
Provides: texlive-doc-th = %{tl_version}
Conflicts: texlive-doc-th < 2009
Obsoletes: texlive-doc-th < 2009
Provides: texlive-doc-tr = %{tl_version}
Conflicts: texlive-doc-tr < 2009
Obsoletes: texlive-doc-tr < 2009
Provides: texlive-doc-uk = %{tl_version}
Conflicts: texlive-doc-uk < 2009
Obsoletes: texlive-doc-uk < 2009
Provides: texlive-doc-vi = %{tl_version}
Conflicts: texlive-doc-vi < 2009
Obsoletes: texlive-doc-vi < 2009
Provides: texlive-doc-zh = %{tl_version}
Conflicts: texlive-doc-zh < 2009
Obsoletes: texlive-doc-zh < 2009

%description	-n texlive-doc
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files		-n texlive-doc
#texmfdistdir/doc/*
%exclude %{texmfdistdir}/doc/tetex
%if %{enable_asymptote}
%exclude %{texmfdistdir}/doc/asymptote
%endif
%if %{enable_xindy}
%exclude %{texmfdistdir}/doc/xindy
%endif
%{texmfdistdir}/doc

#-----------------------------------------------------------------------

%prep
%setup -q -n texlive-%{mga_tl_timestamp}-texmf-doc
#remove source, as we don't need it and it saves some space
rm -rf texmf-dist/source

#-----------------------------------------------------------------------
%build

#-----------------------------------------------------------------------
%install
mkdir -p %{buildroot}%{texmfdistdir}
cp -lfar texmf-dist/* %{buildroot}%{texmfdistdir}

pushd %{buildroot}%{texmfdistdir}
%if !%{enable_asymptote}
    rm -fr asymptote doc/asymptote doc/info/asy* tex/latex/asymptote
%endif
%if !%{enable_xindy}
    rm -fr xindy doc/xindy scripts/xindy
%endif
    find doc/man \( -name Makefile -o -name \*.pdf \) -exec rm -f {} \;
%if %{with_system_psutils}
    rm -f doc/man/man1/{epsffit,extractres,fixdlsrps,fixfmps,fixmacps,fixpsditps,fixpspps,fixscribeps,fixtpps,fixwfwps,fixwpps,fixwwps,getafm,includeres,psbook,psmerge,psnup,psresize,psselect,pstops}.1
%endif

popd

pushd %{buildroot}%{texmfdistdir}
%if %{with_system_tex4ht}
    rm -fr tex4ht
%endif
    rm -f ls-R README
    # .in files in documentation confuse find-provides
    rm -f doc/bibtex/urlbst/*.in
popd

rm -rf %{buildroot}%{texmfdistdir}/man
rm -rf %{buildroot}%{texmfdistdir}/info

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete


#-----------------------------------------------------------------------


%changelog
* Mon Mar 05 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt2_2
- repocop NMU

* Fri Mar 02 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt1_2
- new version

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
