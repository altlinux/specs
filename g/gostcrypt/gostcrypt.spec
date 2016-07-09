Name: 	  gostcrypt
Version:  1.3
Release:  alt1

Summary:  Fork of the (late) Truecrypt project
License:  GPLv3
Group:    Other
Url: 	  http://www.gostcrypt.org/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   GostCrypt_Linux_%version.tar.gz

BuildRequires: gcc-c++ libfuse-devel libwxGTK-devel

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

%build
%make_build NOTEST=1

%install
install -Dm0755 Main/%name %buildroot%_bindir/%name

%check
#./Main/gostcrypt --text --test

%files
%doc README.md Contributors.md License.txt Release/Setup\ Files/GostCryptUserGuide.pdf
%_bindir/%name

%changelog
* Sat Jul 09 2016 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- New version

* Sat Oct 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for ALT Linux
