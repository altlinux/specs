Name: CanFestival-3-source
Version: 2015.08.03
Release: alt2

Summary: Free CanOpen stack
License: GPLv2+
Group: Development/Other
Url: https://hg.beremiz.org/CanFestival-3

Packager: Anton Midyukov <antohami@altlinux.org>

Source: CanFestival-3-%version.tar

Buildarch: noarch

%add_python_req_skip gnosis

%description
Free CanOpen stack.

%prep
%setup -n CanFestival-3-%version
rm -fr debian

# fix shebang
for i in $(find -name '*.py'); do
	sed -i 's|/usr/bin/env python|%__python|' $i
done

%build

%install
mkdir -p %buildroot%_prefix/src/CanFestival-3
cp -r * %buildroot%_prefix/src/CanFestival-3

%files
%_prefix/src/CanFestival-3

%changelog
* Fri Nov 22 2019 Anton Midyukov <antohami@altlinux.org> 2015.08.03-alt2
- fix shebang for *.py

* Sat Mar 10 2017 Anton Midyukov <antohami@altlinux.org> 2015.08.03-alt1
- Initial build for ALT Sisyphus
