%define unicodedir %_datadir/unicode
%define emojidir %unicodedir/emoji
%define unicode_ver 16.0.0
%define emoji_ver 16.0

Name: unicode-emoji
Version: %emoji_ver
Release: alt1

Summary: Unicode Emoji Data Files
Group: Development/Other
License: MIT
Url: https://www.unicode.org/Public/emoji

Source: %url/%version/ReadMe.txt
Source1: https://www.unicode.org/Public/%unicode_ver/ucd/emoji/emoji-data.txt
Source2: %url/%version/emoji-sequences.txt
Source3: %url/%version/emoji-test.txt
Source4: https://www.unicode.org/Public/%unicode_ver/ucd/emoji/emoji-variation-sequences.txt
Source5: %url/%version/emoji-zwj-sequences.txt

# http://www.unicode.org/terms_of_use.html referenced in ReadMe.txt redirects to:
Source6: http://www.unicode.org/copyright.html

BuildArch: noarch

%description
Unicode Emoji Data Files are the machine-readable
emoji data files associated with
http://www.unicode.org/reports/tr51/index.html

%prep
%setup -cT
grep -q "Version[: ]%version" %_sourcedir/{emoji-*,ReadMe}.txt || (echo "text files seems not %version" ; exit 1)

%install
mkdir -p %buildroot%emojidir
cp -a %_sourcedir/emoji-*.txt %buildroot%emojidir
cp -a %_sourcedir/{copyright.html,ReadMe.txt} .

%files
%emojidir/
%doc copyright.html ReadMe.txt

%changelog
* Wed Aug 28 2024 Yuri N. Sedunov <aris@altlinux.org> 16.0-alt1
- 16.0

* Fri Sep 15 2023 Yuri N. Sedunov <aris@altlinux.org> 15.1-alt1
- 15.1

* Fri Sep 23 2022 Yuri N. Sedunov <aris@altlinux.org> 15.0-alt1
- 15.0

* Sun Sep 26 2021 Yuri N. Sedunov <aris@altlinux.org> 14.0-alt1
- 14.0

* Tue Mar 17 2020 Yuri N. Sedunov <aris@altlinux.org> 13.0-alt1
- 13.0

* Thu Aug 22 2019 Yuri N. Sedunov <aris@altlinux.org> 12.0-alt1
- first build for sisyphus


