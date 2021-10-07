Name: 	  gostcrypt
Version:  1.3
Release:  alt5

Summary:  Fork of the (late) Truecrypt project
License:  GPLv3
Group:    Other
Url: 	  http://www.gostcrypt.org/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   GostCrypt_Linux_%version.tar.gz
Patch:    gostcrypt-fix-conversion.patch

BuildRequires: gcc-c++ libfuse-devel libwxGTK3.1-devel

%description
The Gostcrypt project has been launched at the end of 2013 as fork of
the (late) Truecrypt project. Snowden's leaks have made clear more than
ever that the massive use of encryption by citizens must become a
reality. This is possible only if there is a vast, rich offer of
trusted, open source products like Truecrypt, with the strong support of
the hacker community. However, at that time we did not foresee the
unprecedented upheaval of terrible shock with the recent Truecrypt
disappearance. More than ever we all need more and more projects to
replace it. Gostcrypt is one among (we hope) many others. The variety
and richness of encryption solutions is THE solution.

%prep
%setup -n GostCrypt_Linux_%version
%patch -p2

%build
export GST_EXTRA_CFLAGS="-Wno-narrowing -fgnu89-inline -std=gnu++14"
export GST_EXTRA_CXXFLAGS="-Wno-narrowing -fgnu89-inline -std=gnu++14"
%make_build NOTEST=1

%install
install -Dm0755 Main/%name %buildroot%_bindir/%name

%check
#./Main/gostcrypt --text --test

%files
%doc README.md Contributors.md License.txt Release/Setup\ Files/GostCryptUserGuide.pdf
%_bindir/%name

%changelog
* Thu Oct 07 2021 Andrey Cherepanov <cas@altlinux.org> 1.3-alt5
- Rebuild with libwxGTK3.1-devel.

* Thu Sep 23 2021 Andrey Cherepanov <cas@altlinux.org> 1.3-alt4
- FTBFS: fix build with gcc11.

* Mon May 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt3
- NMU: fixed build with current toolchain.

* Sun Jun 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.3-alt2
- Ignore narrowing conversion warnings
- Fix some conversion errors

* Sat Jul 09 2016 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- New version

* Sat Oct 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for ALT Linux
