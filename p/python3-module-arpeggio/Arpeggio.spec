%define oname arpeggio

Name: python3-module-%oname
Version: 1.9.2
Release: alt2

Summary: Parser interpreter based on PEG grammars written in Python
License: MIT
Group: Development/Python3
Url: https://github.com/igordejanovic/Arpeggio
BuildArch: noarch

Source0: v%version.tar.gz

BuildRequires: python3-module-livereload python3-module-mkdocs


%description
Arpeggio is a recursive descent parser with memoization based on PEG
grammars (aka Packrat parser).

%prep
%setup -n Arpeggio-%version

%build
%python3_build_debug -b build3

mkdocs.py3 build

%install
rm -rf build && ln -sf build3 build
%python3_install

%files
%doc site examples
%python3_sitelibdir_noarch/%oname
%python3_sitelibdir_noarch/Arpeggio-*.egg-info


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.ru> 1.9.2-alt2
- disable python2

* Sat Oct 26 2019 Fr. Br. George <george@altlinux.ru> 1.9.2-alt1
- Autobuild version bump to 1.9.2

* Mon Jan 28 2019 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1
- Autobuild version bump to 1.9.0

* Thu Jun 14 2018 Fr. Br. George <george@altlinux.ru> 1.8.0-alt1
- Autobuild version bump to 1.8.0

* Thu Jun 14 2018 Fr. Br. George <george@altlinux.ru> 1.7.1-alt1
- Initial build for ALT

