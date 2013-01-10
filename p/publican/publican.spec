# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBI.pm) perl(IO/String.pm) perl(List/Util.pm) perl(Pod/Usage.pm) perl(Time/localtime.pm) perl(Unicode/Collate.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Requires: docbook-dtds docbook-style-xsl
BuildRequires: docbook-dtds docbook-style-xsl

# Track font name changes
%define RHEL6 %([[ %{?dist}x == .el6[a-z]* ]] && echo 1 || echo 0)
# Assume not rhel means FC11+ ... ugly
%define OTHER 1

%if %{RHEL6}
%define OTHER 0
%endif

# required for desktop file install
%define my_vendor %(test %{OTHER} == 1 && echo "fedora" || echo "redhat")

%define TESTS 0

Name:           publican
Version:        2.8
Release:        alt2_4
Summary:        Common files and scripts for publishing with DocBook XML
# For a breakdown of the licensing, refer to LICENSE
License:        (GPLv2+ or Artistic) and CC0
Group:          Publishing
URL:            https://publican.fedorahosted.org
Source0:        https://fedorahosted.org/released/publican/Publican-%{version}.tar.gz
# Limited to these arches on RHEL 6 due to PDF + Java limitations
%if %{RHEL6}
ExclusiveArch:   i686 x86_64
%else
BuildArch:      noarch
%endif

# Get rid of the old packages
Obsoletes:      perl-Publican-WebSite
Obsoletes:      publican-WebSite-obsoletes
Conflicts: perl-Publican-WebSite
Conflicts: publican-WebSite-obsoletes
# Do NOT support very old packages
#Provides:       perl-Publican-WebSite = 1.5
#Provides:       publican-WebSite-obsoletes = 1.21

BuildRequires:  perl(Devel/Cover.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Test/Perl/Critic.pm)
BuildRequires:  perl(Archive/Tar.pm)
BuildRequires:  perl(Archive/Zip.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Config/Simple.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Format/DateParse.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(File/Copy/Recursive.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Find/Rule.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/pushd.pm)
BuildRequires:  perl(File/Which.pm)
BuildRequires:  perl(HTML/FormatText.pm)
BuildRequires:  perl(HTML/TreeBuilder.pm)
BuildRequires:  perl(I18N/LangTags/List.pm)
BuildRequires:  perl(Image/Magick.pm)
BuildRequires:  perl(Image/Size.pm)
BuildRequires:  perl(Locale/Maketext/Gettext.pm)
BuildRequires:  perl(Locale/Language.pm)
BuildRequires:  perl(Locale/PO.pm)
BuildRequires:  perl(Makefile/Parser.pm)
BuildRequires:  perl(Syntax/Highlight/Engine/Kate.pm)
BuildRequires:  perl(Term/ANSIColor.pm)
BuildRequires:  perl(Text/Wrap.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(version.pm)
BuildRequires:  perl(XML/LibXML.pm)
BuildRequires:  perl(XML/LibXSLT.pm)
BuildRequires:  perl(XML/Simple.pm)
BuildRequires:  perl(XML/TreeBuilder.pm)
BuildRequires:  fop
BuildRequires:  batik
BuildRequires:  docbook-style-xsl >= 1.76.1
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  perl-Template
BuildRequires:  perl(DBD/SQLite.pm)

# Most of these are handled automatically
Requires:       perl(Locale/Maketext/Gettext.pm)
Requires:       fop
Requires:       batik rpm-build
Requires:       docbook-style-xsl >= 1.76.1
Requires:       perl(XML/LibXML.pm) >= 1.67
Requires:       perl(XML/LibXSLT.pm) >= 1.67
Requires:       perl(XML/TreeBuilder.pm) >= 4.0
Requires:       gettext cvs
Requires:       perl-Template
Requires:       perl(DBD/SQLite.pm)
 
# Pull in the fonts for all languages, else you can't build translated PDF in brew/koji
%if %{RHEL6}
Requires:       fonts-ttf-liberation fonts-ttf-liberation fonts-ttf-liberation
Requires:       fonts-ttf-cjkuni-uming fonts-ttf-ipa-gothic fonts-ttf-ipa-pgothic
Requires:       fonts-ttf-lklug fonts-ttf-baekmuk-batang

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

Obsoletes:      Publican < 1.0
Source44: import.info
# Do NOT support very old packages
#Provides:       Publican = 1.0

%description
Publican is a DocBook publication system, not just a DocBook processing tool.
As well as ensuring your DocBook XML is valid, publican works to ensure
your XML is up to publishable standard.

%package doc
Group:          Documentation
Summary:        Documentation for the Publican package
Requires:       xdg-utils
Obsoletes:      Publican-doc < 1.0
# Do NOT support very old packages
#Provides:       Publican-doc = 1.0

%description doc
Publican is a tool for publishing material authored in DocBook XML.
This guide explains how to  to create and build books and articles
using publican. It is not a DocBook XML tutorial and concentrates
solely on using the publican tools.

%prep
%setup -q -n Publican-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build
dir=`pwd` && cd Users_Guide && %{__perl} -CA -I $dir/blib/lib $dir/blib/script/publican build \
    --formats=html-desktop --publish --langs=all \
    --common_config="$dir/blib/datadir" \
    --common_content="$dir/blib/datadir/Common_Content"

%install

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


./fop-ttc-metric.pl --outdir $RPM_BUILD_ROOT%{_datadir}/publican/fop/font-metrics --conffile $RPM_BUILD_ROOT%{_datadir}/publican/fop/fop.xconf

sed -i -e 's|@@FILE@@|%{_docdir}/%{name}-doc-%{version}/en-US/index.html|' %{name}.desktop
sed -i -e 's|@@ICON@@|%{_docdir}/%{name}-doc-%{version}/en-US/images/icon.svg|' %{name}.desktop

desktop-file-install --vendor="%{my_vendor}" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop

for file in po/*.po; do
    lang=`echo "$file" | sed -e 's/po\/\(.*\)\.po/\1/'`;
    mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES;
    msgfmt $file -o $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/%{name}.mo;
done

%find_lang %{name}

%check
%if %{TESTS}
./Build test
%endif

%files -f %{name}.lang
%doc CHANGES README COPYING Artistic
%{perl_vendor_privlib}/Publican.pm
%{perl_vendor_privlib}/Publican/*
%{_mandir}/man1/*
%{_bindir}/publican
%{_datadir}/publican
%config(noreplace) %{_datadir}/publican/default.db
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/publican-website.cfg
%config(noreplace) %{_sysconfdir}/bash_completion.d/_publican

%files doc
%doc Users_Guide/publish/desktop/*
%{_datadir}/applications/%{my_vendor}-%{name}.desktop
%doc fdl.txt

%changelog
* Thu Jan 10 2013 Igor Vlasenko <viy@altlinux.ru> 2.8-alt2_4
- added Req: docbook-dtds

* Thu Jan 10 2013 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_4
- initial fc import

