Name: lzip
Version: 1.13
Release: alt2

Summary: LZMA file compressor
License: GPL v3+
Group: Archiving/Compression

Url: http://savannah.nongnu.org/projects/lzip/
Source: http://download.savannah.gnu.org/releases/lzip/%name-%version.tar.gz
Source100: lzip.watch
Patch: %name-info.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Sep 20 2009
BuildRequires: gcc-c++

Summary(pl.UTF-8): Kompresor plików oparty na algorytmie LZMA

%description
Lzip is a lossless file compressor based on the LZMA
(Lempel-Ziv-Markov chain-Algorithm) algorithm designed by Igor Pavlov.
The high compression of LZMA comes from combining two basic,
well-proven compression ideas: sliding dictionaries (i.e. LZ77/78),
and Markov models (i.e. the thing used by every compression algorithm
that uses a range encoder or similar order-0 entropy coder as its last
stage) with segregation of contexts according to what the bits are
used for.

%description -l pl.UTF-8
lzip to bezstratny kompresor plików oparty na algorytmie LZMA
(Lempel-Ziv-Markov chain-Algorithm) opracowanym przez Igora Pawłowa.
Wysoki stopień kompresji LZMA wywodzi się z połączenia dwóch
podstawowych, dobrze sprawdzonych idei kompresji: przesuwnych
słowników (LZ77/78) i modeli Markowa (używanych przez każdy
algorytm kompresji wykorzystujący w ostatnim stadium kodowanie
zakresów lub podobne kodowanie entropii rzędu 0) z podziałem
kontekstów w zależności od wykorzystania bitów.

%prep
%setup
%patch -p1

%build
%configure
make all info

%install
%makeinstall_std install-man

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/lz*
%_man1dir/lzip.1*
%_infodir/lzip.info*

%changelog
* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 1.13-alt2
- added watch file

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 1.13-alt1
- 1.13
  + lziprecover moved to a separate tarball

* Sat Sep 24 2011 Michael Shigorin <mike@altlinux.org> 1.12-alt1
- 1.12

* Sun Sep 20 2009 Michael Shigorin <mike@altlinux.org> 1.8-alt1
- initial build for ALT Linux Sisyphus (spec from PLD) (closes: #18124)
