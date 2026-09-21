%define dname fonts-Fast

Name:	 fonts-ttf-Fast
Epoch:	 1
Version: 0.0.0
Release: alt1.b2cfd87d

Summary: Free Fast-Font fonts for faster reading
License: MIT
Group:   System/Fonts/True type
URL:     https://github.com/Born2Root/Fast-Font
VCS:     https://github.com/Born2Root/Fast-Font

Source:  %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-fonts

%description
This font provides faster reading through facilitating the reading process
by guiding the eyes through text with artificial fixation points. As a result,
the reader is only focusing on the highlighted initial letters and lets the
brain center complete the word. This allows you to read in supersonic speed.
At the moment we have four different variations of the Fast-Font available.
The first three are best suited for reading and offer support for the most
languages.
The Monospaced version is the best fit if you want to use
it in an coding environment:
1. Fast Font with Serifs;
2. Fast Font Sans (without Serifs);
3. Fast Font Sans (without Serifs) and Dots as spaces;
4. Fast Font Monospaced.

%prep
%setup

%build

%install
%ttf_fonts_install %dname

%files -f %dname.files
%doc *.md LICENSE *.gif *.jpg

%changelog
* Tue Sep 15 2026 Polina Poidenko <polipoki@altlinux.org> 1:0.0.0-alt1.b2cfd87d
- Changed to correct version using the commit hash.
- Added LICENSE and missing elements for the README.

* Tue Sep 23 2025 Polina Poidenko <polipoki@altlinux.org> 20250121-alt1
- Initial build for Sisyphus (Closes: 53060).
