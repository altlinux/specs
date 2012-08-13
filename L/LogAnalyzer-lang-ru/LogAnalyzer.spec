Name: LogAnalyzer-lang-ru
Version: 3.4.4
Release: alt2

Summary: Russian interfacetranslation for LogAnalyzer
License: GPLv3+
Group: Monitoring

Url: http://loganalyzer.adiscon.com
Source: %name-main.php
BuildArch: noarch

Requires: LogAnalyzer >= 3.4.0

%define origname LogAnalyzer
%define wwwdir %_datadir/%origname
%define lang ru
%define langdir %wwwdir/lang/%lang
%define langinfo Russian

%description
This package provides %langinfo translation for LogAnalyzer.

%prep

%build

%install
install -pDm644 %SOURCE0 %buildroot%langdir/main.php
ln -s ../en/admin.php %buildroot%langdir/admin.php
echo %langinfo > %buildroot%langdir/info.txt

%files
%langdir/*

%changelog
* Mon Aug 13 2012 Michael Shigorin <mike@altlinux.org> 3.4.4-alt2
- workaround php5-jpgraph/fonts-ttf-vera deficiency wrt cyrillics

* Mon Aug 13 2012 Michael Shigorin <mike@altlinux.org> 3.4.4-alt1
- initial release (only main.php is translated)
