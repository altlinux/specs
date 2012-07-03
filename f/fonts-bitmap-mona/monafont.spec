%define oldname monafont
%{!?_fontbasedir: %global _fontbasedir %{_datadir}/fonts}

%define		archivename		monafont

%define		projectname		mona
%define		fontname		%{projectname}
%define		family_ttf_s		sazanami
%define		family_ttf_v		vlgothic
%define		real_family_ttf_s	sazanami
%define		real_family_ttf_v	VLGothic

%define		rpmname_suffix	fonts

%define		fontdir_bitmap	%{projectname}-bitmap
%define		fontdir_ttf_s		%{projectname}-%{family_ttf_s}
%define		fontdir_ttf_v		%{projectname}-%{family_ttf_v}

%define		name_bitmap		fonts-bitmap-%{fontdir_bitmap}
%define		name_ttf_s		fonts-ttf-%{fontdir_ttf_s}
%define		name_ttf_v		fonts-ttf-%{fontdir_ttf_v}

%define		old_name_bitmap	mona-fonts-bitmap
%define		old_name_ttf_s	mona-fonts-sazanami
%define		old_name_ttf_v	mona-fonts-VLGothic

%define		fontdir_bitmap_full	%{_fontbasedir}/bitmap/%{fontdir_bitmap}
%define		fontdir_ttf_s_full	%{_fontbasedir}/ttf/%{fontdir_ttf_s}
%define		fontdir_ttf_v_full	%{_fontbasedir}/ttf/%{fontdir_ttf_v}

%define		obsoletes_EVR		2.90-5.999
%define		sazanami_ver		20040629
%define		vlgothic_ver		20111122

%define		catalog_dir		%{_sysconfdir}/X11/fontpath.d

# misc
%define		show_progress		0

%define	common_description	\
Mona Font is a Japanese proportional font which allows you to view \
Japanese text arts correctly.

Name:		fonts-bitmap-mona
Version:	2.90
Release:	alt1_15
Summary:	Japanese font for text arts

# monafont itself is under public domain
Group:		Graphical desktop/Other
License:	Public Domain
URL:		http://monafont.sourceforge.net/
Source0:	http://downloads.sourceforge.net/monafont/%{archivename}-%{version}.tar.bz2
# Need investigating, however
# it seems that the behavior of "split" changed between 5.10 -> 5.12
Patch0:	monafont-2.90-perl512-split.patch

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info

%description
%{common_description}

%package -n	%{name_bitmap}
Summary:	Bitmap Japanese font for text arts
Group:		Graphical desktop/Other
License:	Public Domain
# Write BuildRequires a bit verbosely
BuildRequires:	perl
BuildRequires:	xorg-x11-font-utils
Obsoletes:	%{old_name_bitmap} <= %{obsoletes_EVR}
Provides:	%{old_name_bitmap} = %{version}-%{release}

%description -n	%{name_bitmap}
%{common_description}

%package -n	%{name_ttf_s}
Summary:	True Type Japanese font for text arts based on Sazanami
Group:		Graphical desktop/Other
# monafont itself is Public Domain and this package borrows
# sazanami
# And the outline otf uses Kochi-substitute (later renamed to sazanami),
# which is under BSD
License:	BSD
BuildRequires:	fonts-ttf-sazanami-gothic = 0.%{sazanami_ver}

%description -n	%{name_ttf_s}
%{common_description}

This package contains True Type fonts generated generated from
%{oldname} source package which are based on Sazanami fonts.

%package -n	%{name_ttf_v}
Summary:	True Type Japanese font for text arts based on VLGothic
Group:		Graphical desktop/Other
# monafont itself is Public Domain and this package borrows
# VLGothic (mplus and BSD)
# And the outline otf uses Kochi-substitute (later renamed to sazanami),
# which is under BSD
License:	mplus and BSD
BuildRequires:	fonts-ttf-vlgothic-p >= %{vlgothic_ver}

%description -n	%{name_ttf_v}
%{common_description}

This package contains True Type fonts generated generated from
%{oldname} source package which are based on VLGothic fonts.

%prep
%setup -q -n %{oldname}-%{version}
%patch0 -p1 -b .perl512

iconv -f EUC-JP -t UTF-8 README.euc > README
touch -r README.euc README
iconv -f SHIFT-JIS -t UTF-8 ttfsrc/README-ttf.txt > ttfsrc/README-ttf.txt.tmp
touch -r ttfsrc/README-ttf.txt ttfsrc/README-ttf.txt.tmp
mv -f ttfsrc/README-ttf.txt.tmp ttfsrc/README-ttf.txt

%if ! %{show_progress}
# In the build on koji, showing progress bar is rather dirty
grep -rl '\\rprogress' . | xargs sed -i.bar -e '/\\rprogress/s|print|# print|'
%endif


%build
## Not using parallel make

# 1. bitmap fonts
make bdf

%if 0
# 2. ttf
cd ttfsrc
cp -p name.src name.src.orig

## 2.1 ttf based on sazanami
sed -e 's|^Mona$|Mona-%{real_family_ttf_s}|' name.src.orig > name.src
#make clean
make \
	BASE_OUTLINE_TTF=$(find %{_fontbasedir}/%{family_ttf_s} -name sazanami-gothic.ttf) \
	BASE_OUTLINE_VERSION=%{real_family_ttf_s}-%{sazanami_ver}
mv mona.ttf mona-%{real_family_ttf_s}.ttf

## 2.2 ttf based on VLGothic
sed -e 's|^Mona$|Mona-%{real_family_ttf_v}|' name.src.orig > name.src
make clean
make \
	BASE_OUTLINE_TTF=$(find %{_fontbasedir}/%{family_ttf_v} -name VL-PGothic-Regular.ttf) \
	BASE_OUTLINE_VERSION=%{real_family_ttf_v}-%{vlgothic_ver}
mv mona.ttf mona-%{real_family_ttf_v}.ttf

cd ..
%endif

%install

# 1. bitmap fonts
mkdir -p -m 0755 $RPM_BUILD_ROOT%{fontdir_bitmap_full}
make install \
	X11BINDIR=%{_bindir} \
	MKDIRHIER="mkdir -p" \
	X11FONTDIR=$RPM_BUILD_ROOT%{fontdir_bitmap_full} \
	GZIP_CMD="gzip -9" \
	install
install -cpm 644 fonts.alias.mona \
	$RPM_BUILD_ROOT%{fontdir_bitmap_full}/fonts.alias

## catalog symlink
mkdir -p $RPM_BUILD_ROOT%{catalog_dir}
pushd $RPM_BUILD_ROOT%{catalog_dir}

UPWARDDIR="../../.."
ln -sf ${UPWARDDIR}%{fontdir_bitmap_full} %{fontdir_bitmap}
if [ ! -f $UPWARDDIR%{fontdir_bitmap_full}/fonts.dir ] ; then
	echo "Perhaps symlink target is wrong"
	exit 1
fi
popd

%if 0
# 2. ttf
cd ttfsrc

mkdir -p -m 0755 $RPM_BUILD_ROOT%{fontdir_ttf_s_full}
install -cpm 0644 mona-%{real_family_ttf_s}.ttf $RPM_BUILD_ROOT%{fontdir_ttf_s_full}/

mkdir -p -m 0755 $RPM_BUILD_ROOT%{fontdir_ttf_v_full}
install -cpm 0644 mona-%{real_family_ttf_v}.ttf $RPM_BUILD_ROOT%{fontdir_ttf_v_full}/
%endif

cd ..
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi

%files -n	%{name_bitmap}
%doc	README
%doc	README.ascii

%{catalog_dir}/%{fontdir_bitmap}*
%dir				%{fontdir_bitmap_full}
%verify(not md5 size mtime)	%{fontdir_bitmap_full}/fonts.alias
%verify(not md5 size mtime)	%{fontdir_bitmap_full}/fonts.dir
%{fontdir_bitmap_full}/*.pcf.gz

%if 0
%files -n %{name_ttf_s}
%define	_font_pkg_name	%{name_ttf_s}
%define	_fontdir	%{fontdir_ttf_s_full}
%{_fontbasedir}/*/%{_fontstem}/mona-%{real_family_ttf_s}.ttf
%doc	ttfsrc/README-ttf.txt
%files -n %{name_ttf_v}
%define	_font_pkg_name	%{name_ttf_v}
%define	_fontdir	%{fontdir_ttf_v_full}
%{_fontbasedir}/*/%{_fontstem}/mona-%{real_family_ttf_v}.ttf
%doc	ttfsrc/README-ttf.txt
%endif

%changelog
* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.90-alt1_15
- fc import

