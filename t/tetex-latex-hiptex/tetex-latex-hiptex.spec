#%define fname church
%define texmf_dir %_datadir/texmf
%define prefix %texmf_dir
%define fontsbase hiptex
%define texpackname hiptex
#%define type1fonts %_type1fontsdir/%fname

Name: tetex-latex-hiptex
Version: 0.7.1alt
Release: alt0.1.qa1

Summary: LaTeX package for writing Church Slavonic texts in HIP encoding
Summary(ru_RU.KOI8-R): Использование церковно-славянских шрифтов в TeX (кодировка HIP)

License: LPPL
Group: Publishing
Url: http://str12.sobor.org/hip/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

#Source: http://www.sobor.org/hip/%name-%version.tar.bz2
# I use repacked archive
Source: %name-%version.tar.bz2
Patch: %name.patch

#AutoReq: yes, perl
PreReq: tetex-core >= 2.0-alt0.8
Requires: fonts-type1-church

#Requires: church-fonts
Provides: hiptex
Obsoletes: hiptex

#BuildRequires: tetex-latex >= 2.0-alt0.8, tetex-dvips
#BuildRequires: tetex-afm, church-fonts

%package doc
Summary: Documentation for usage of %name
Summary(ru_RU.KOI8-R): Документация по использованию %name
Group: Publishing
Requires: tetex-latex >= 2.0, %name = %version-%release
Provides: hiptex-doc
Obsoletes: hiptex-doc

%description
HIPTeX is a LaTeX package for writing Church Slavonic texts in HIP
encoding. HIP is a system to represent Church Slavonic text using the
standard  Cyrillic alphabet and a small number of ASCII symbols. HIP
was  developed as part of project Pechatnyj Dvor (Printing House)
<http://pechatnyj-dvor.narod.ru/index.html>.

The package includes the hipfonts style, which allows inclusion of
Church Slavonic text in an arbitrary LaTeX document, and the hipbook
class, which provides book definitions corresponding to the
liturgical book conventions of the Russian orthodox church.

%description -l ru_RU.KOI8-R
Пакет %name, позволяющий использовать
церковно-славянские шрифты в TeX. Содержит
класс для создания книг. Предназначен для использования
текстов в кодировке HIP.

%description doc
Documentation for usage of %name

%description doc -l ru_RU.KOI8-R
Документация по использованию %name

%prep
%setup -q
%patch

%build

%install
mkdir -p %buildroot%texmf_dir
cp -a texmf/* %buildroot%texmf_dir/

mkdir -p %buildroot%_sysconfdir/tex-fonts.d
echo "Map hiptex.map" > %buildroot%_sysconfdir/tex-fonts.d/%texpackname.cfg
# /usr/share/texmf/dvips/config/hiptex.map

# TODO: add 'churchslavonic  cshyphts.tex' to
# /usr/share/texmf/tex/generic/config/language.dat

%files doc
%doc doc/* examples/
#%texmf_dir/doc/%texpackname

%files
%doc LICENSE README
%_sysconfdir/tex-fonts.d/*
#%texmf_dir/dvipdfm/*
%texmf_dir/dvips/config/*
%texmf_dir/dvips/base/*
%texmf_dir/fonts/afm/%fontsbase
%texmf_dir/fonts/tfm/%fontsbase
%texmf_dir/fonts/vf/%fontsbase
%texmf_dir/fonts/type1/%fontsbase
%texmf_dir/tex/latex/%texpackname
%texmf_dir/tex/generic/%texpackname
%texmf_dir/tex/generic/babel/churchslavonic.ldf
#%doc LICENSE

%changelog
* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.7.1alt-alt0.1.qa1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for tetex-latex-hiptex
  * postclean-05-filetriggers for spec file

* Sun Apr 15 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.1alt-alt0.1
- new version (0.7.1)
- please, test and fixme

* Mon Jan 05 2004 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt2
- rename to tetex-latex-hiptex
- rebuild

* Fri Apr 04 2003 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- first release for ALT Linux Sisyphus
- Warning! It released with error during dvi to ps conversion :(

