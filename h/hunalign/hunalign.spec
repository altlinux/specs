Name: hunalign
Version: 1.1
Release: alt1

Summary: The hunalign sentence aligner

Group: Text tools
License: LGPL
Url: http://mokk.bme.hu/resources/hunalign/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://ftp.mokk.bme.hu/Hunglish/src/hunalign/latest/%name-%version.tar

# Automatically added by buildreq on Mon Apr 16 2012
# optimized out: libstdc++-devel
BuildRequires: gcc-c++

%description
hunalign aligns bilingual text on the sentence level. Its input is
tokenized and sentence-segmented text in two languages. In the simplest
case, its output is a sequence of bilingual sentence pairs (bisentences).

In the presence of a dictionary, hunalign uses it, combining this
information with Gale-Church sentence-length information. In the absence
of a dictionary, it first falls back to sentence-length information,
and then builds an automatic dictionary based on this alignment. Then
it realigns the text in a second pass, using the automatic dictionary.

Like most sentence aligners, hunalign does not deal with changes of
sentence order: it is unable to come up with crossing alignments, i.e.,
segments A and B in one language corresponding to segments B' A' in
the other language.

There is nothing Hungarian-specific in hunalign, the name simply reflects
the fact that it is part of the hun* NLP toolchain.

%package data
Summary: Data files for %name
Group: Text tools
Requires: %name = %version-%release
BuildArch: noarch

%description data
This package contain data files for %name


%prep
%setup

%build
cd src/hunalign
%make_build

%install
install src/hunalign/%name -D %buildroot%_bindir/%name
mkdir -p %buildroot%_datadir/%name/
cp -a data/ %buildroot%_datadir/%name/

%files
%doc readme.html examples/ scripts/
%_bindir/%name

%files data
%_datadir/%name/

%changelog
* Mon Apr 16 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus
