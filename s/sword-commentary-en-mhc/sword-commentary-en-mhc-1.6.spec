Name: sword-commentary-en-mhc
Version: 1.6
Release: alt1

Summary: Matthew Henry's Complete Commentary on the Whole Bible for SWORD
License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.2

%description
Matthew Henry's Complete Commentary on the Whole Bible
Public Domain--Copy Freely.
This text was prepared from the Christian Classics Ethereal Library
located at www.ccel.org.
Thanks also to Logos Research, Inc. for providing CCEL with their text
of Matthew Henrey's Complete Commentary, from which this edition has
been prepared.

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%prep
%setup -q

%install
mkdir -p %buildroot%_datadir/sword
unzip *.zip -d %buildroot%_datadir/sword

%files
%_datadir/sword/

%changelog
* Tue Jun 13 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.6-alt1
- initial build for Sisyphus
