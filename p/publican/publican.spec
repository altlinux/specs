# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Unicode/Collate.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Requires: docbook-dtds docbook-style-xsl perl-Makefile-Parser
BuildRequires: docbook-dtds docbook-style-xsl

# Track font name changes
%define RHEL6 %([[ %{?dist}x == .el6[a-z]* ]] && echo 1 || echo 0)

%define OTHER 1
%if %{RHEL6}
%define OTHER 0
%endif

# required for desktop file install
%define my_vendor %(test %{OTHER} == 1 && echo "fedora" || echo "redhat")

%define TESTS 0
%define brand common
%define wwwdir /var/www/html/docs

Name:           publican
Version:        3.0.0
Release:        alt1_0
Summary:        Common files and scripts for publishing with DocBook XML
# For a breakdown of the licensing, refer to LICENSE
License:        (GPLv2+ or Artistic) and CC0
Group:          Publishing
URL:            https://publican.fedorahosted.org
Source0:        https://fedorahosted.org/released/publican/Publican-v%{version}.tar.gz
BuildArch:      noarch

# Get rid of the old packages
Obsoletes:      perl-Publican-WebSite
Obsoletes:      publican-WebSite-obsoletes
Conflicts:      perl-Publican-WebSite
Conflicts:      publican-WebSite-obsoletes

## work around arch -> noarch bug in yum
Obsoletes:      publican < 3

BuildRequires:  perl(Devel/Cover.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Archive/Tar.pm)
BuildRequires:  perl(Archive/Zip.pm)
BuildRequires:  perl(Locale/Maketext/Gettext.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Config/Simple.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Format/DateParse.pm)
BuildRequires:  perl(DBI.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Copy/Recursive.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Find/Rule.pm)
BuildRequires:  perl(File/HomeDir.pm)
BuildRequires:  perl(File/Inplace.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/pushd.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Which.pm)
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(HTML/FormatText.pm)
BuildRequires:  perl(HTML/FormatText/WithLinks.pm)
BuildRequires:  perl(HTML/FormatText/WithLinks/AndTables.pm)
BuildRequires:  perl(HTML/TreeBuilder.pm)
BuildRequires:  perl(I18N/LangTags/List.pm)
BuildRequires:  perl(IO/String.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Locale/Language.pm)
BuildRequires:  perl(Locale/PO.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Pod/Usage.pm)
BuildRequires:  perl(String/Similarity.pm)
BuildRequires:  perl(Syntax/Highlight/Engine/Kate.pm)
BuildRequires:  perl(Template.pm)
BuildRequires:  perl(Template/Constants.pm)
BuildRequires:  perl(Term/ANSIColor.pm)
BuildRequires:  perl(Text/Wrap.pm)
BuildRequires:  perl(Time/localtime.pm)
BuildRequires:  perl(XML/LibXML.pm)
BuildRequires:  perl(XML/LibXSLT.pm)
BuildRequires:  perl(XML/Simple.pm)
BuildRequires:  perl(XML/TreeBuilder.pm)
BuildRequires:  wkhtmltopdf
BuildRequires:  docbook-style-xsl >= 1.76.1
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  perl(Text/CSV_XS.pm)

# Most of these are handled automatically
Requires:       perl(Locale/Maketext/Gettext.pm)
Requires:       wkhtmltopdf
Requires:       rpm-build
Requires:       docbook-style-xsl >= 1.76.1
Requires:       perl(XML/LibXML.pm) >= 1.67
Requires:       perl(XML/LibXSLT.pm) >= 1.67
Requires:       perl(XML/TreeBuilder.pm) >= 4.0
Requires:       perl-Template
Requires:       perl(DBD/SQLite.pm)
Requires:       perl(Text/CSV_XS.pm)

# Lets validate some basics

# Pull in the fonts for all languages, else you can't build translated PDF in brew/koji
%if %{RHEL6}
Requires:       fonts-ttf-liberation fonts-ttf-liberation fonts-ttf-liberation
Requires:       fonts-ttf-cjkuni-uming fonts-ttf-ipa-gothic fonts-ttf-ipa-pgothic
Requires:       fonts-ttf-lklug fonts-ttf-baekmuk-batang
Requires:       fonts-ttf-lohit-assamese fonts-ttf-lohit-bengali fonts-ttf-lohit-devanagari
Requires:       fonts-ttf-lohit-gujarati lohit-hindi-fonts fonts-ttf-lohit-kannada
Requires:       lohit-kashmiri-fonts lohit-konkani-fonts lohit-maithili-fonts
Requires:       fonts-ttf-lohit-malayalam fonts-ttf-lohit-marathi fonts-ttf-lohit-nepali
Requires:       fonts-ttf-lohit-oriya fonts-ttf-lohit-punjabi lohit-sindhi-fonts
Requires:       fonts-ttf-lohit-tamil fonts-ttf-lohit-telugu dejavu-lgc-sans-mono-fonts
Requires:       dejavu-fonts-common fonts-ttf-dejavu fonts-ttf-dejavu
Requires:       fonts-ttf-dejavu

BuildRequires:  fonts-ttf-liberation fonts-ttf-liberation fonts-ttf-liberation
BuildRequires:  fonts-ttf-cjkuni-uming fonts-ttf-ipa-gothic fonts-ttf-ipa-pgothic
BuildRequires:  fonts-ttf-lklug fonts-ttf-baekmuk-batang
%endif
%if %{OTHER}
Requires:       fonts-ttf-liberation fonts-ttf-liberation fonts-ttf-liberation
Requires:       fonts-ttf-cjkuni-uming fonts-ttf-ipa-gothic fonts-ttf-ipa-pgothic
Requires:       fonts-ttf-lklug fonts-ttf-baekmuk-batang

BuildRequires:  fonts-ttf-liberation fonts-ttf-liberation fonts-ttf-liberation
BuildRequires:  fonts-ttf-cjkuni-uming fonts-ttf-ipa-gothic fonts-ttf-ipa-pgothic
BuildRequires:  fonts-ttf-lklug fonts-ttf-baekmuk-batang
%endif
Source44: import.info

%description
Publican is a DocBook publication system, not just a DocBook processing tool.
As well as ensuring your DocBook XML is valid, publican works to ensure
your XML is up to publishable standard.

%package doc
Group:          Documentation
Summary:        Documentation for the Publican package
Requires:       xdg-utils
Obsoletes:      publican-doc < 3

%description doc
Publican is a tool for publishing material authored in DocBook XML.
This guide explains how to  to create and build books and articles
using publican. It is not a DocBook XML tutorial and concentrates
solely on using the publican tools.

%package common-web
Group:          Documentation
Summary:        Website style for common brand
Requires:       publican

%description common-web
Website style for common brand.

%prep
%setup -q -n Publican-v%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor --nocolours=1
./Build
dir=`pwd` && cd Users_Guide && %{__perl} -CA -I $dir/blib/lib $dir/blib/script/publican build \
    --formats=html-desktop --publish --langs=all \
    --common_config="$dir/blib/datadir" \
    --common_content="$dir/blib/datadir/Common_Content" --nocolours

%install

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

sed -i -e 's|@@FILE@@|%{_docdir}/%{name}-doc-%{version}/en-US/index.html|' %{name}.desktop
sed -i -e 's|@@ICON@@|%{_docdir}/%{name}-doc-%{version}/en-US/images/icon.svg|' %{name}.desktop

desktop-file-install --vendor="%{my_vendor}" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop

for file in po/*.po; do
    lang=`echo "$file" | sed -e 's/po\/\(.*\)\.po/\1/'`;
    mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES;
    msgfmt $file -o $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/%{name}.mo;
done

%find_lang %{name}

# Package web common files
mkdir -p -m755 $RPM_BUILD_ROOT/%{wwwdir}/%{brand}
dir=`pwd`
cd datadir/Common_Content/common
%{__perl} -CA -I $dir/blib/lib $dir/blib/script/publican install_brand --web --path=$RPM_BUILD_ROOT/%{wwwdir}/%{brand}
cd -
sed -i -e '1,4s,perl[0-9a-z\.]*,perl,' %buildroot%_bindir/publican

%check
%if %{TESTS}
./Build test
%endif

%post
CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "https://fedorahosted.org/released/publican/xsl/docbook4/" \
 "file://%{_datadir}/publican/xsl/"  $CATALOG

%postun
if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
   "file://%{_datadir}/publican/xsl/docbook4/" $CATALOG
fi

%files -f %{name}.lang
%doc Changes README COPYING Artistic pod1/publican
%{perl_vendor_privlib}/Publican.pm
%{perl_vendor_privlib}/Publican/*
%{_mandir}/man1/*
%{_bindir}/publican
%{_bindir}/db5-valid
%{_bindir}/db4-2-db5
%{_datadir}/publican
%config(noreplace) %{_datadir}/publican/default.db
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/publican-website.cfg
%config(noreplace) %{_sysconfdir}/bash_completion.d/_publican

%files doc
%doc Users_Guide/publish/desktop/*
%{_datadir}/applications/%{my_vendor}-%{name}.desktop
%doc fdl.txt

%files common-web
%{wwwdir}/%{brand}


%changelog
* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_0
- update to new release by fcimport

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.8-alt4_5
- fixed perl specific build

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 2.8-alt3_5
- update to new release by fcimport

* Thu Jan 10 2013 Igor Vlasenko <viy@altlinux.ru> 2.8-alt3_4
- added Req: on perl-Makefile-Parser

* Thu Jan 10 2013 Igor Vlasenko <viy@altlinux.ru> 2.8-alt2_4
- added Req: docbook-dtds

* Thu Jan 10 2013 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_4
- initial fc import

