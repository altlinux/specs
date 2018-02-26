Summary: Example files for littlewizard
Name: littlewizard-examples
Version: 20071206
Release: alt1
License: GPL
Group: Education
Url: http://littlewizard.sourceforge.net/
Packager: Fr. Br. George <george@altlinux.ru>
Source: http://dl.sf.net/littlewizard/examples-%version.zip
BuildRequires: unzip

BuildArch: noarch

%description
Little Wizard is created especially for primary school children. It allows to
learn using main elements of present computer languages, including: variables,
expressions, loops, conditions, logical blocks. Every element of language is
represented by an intuitive icon. It allows program Little Wizard without
using keyboard, only mouse.

This package contains example files for Little Wizard.

%prep
%setup -q -n examples-%version

mkdir -p %buildroot%_datadir/littlewizard/examples
install -p -m644 *.lwp %buildroot%_datadir/littlewizard/examples

%files
%_datadir/littlewizard/examples

%changelog
* Mon Jul 21 2008 Fr. Br. George <george@altlinux.ru> 20071206-alt1
Initial build

