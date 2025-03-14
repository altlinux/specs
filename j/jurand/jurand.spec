Name: jurand
Version: 1.3.5
Release: alt2

Summary: A tool for manipulating symbols present in Java source files
License: Apache-2.0
Group: Development/Java
Url: https://github.com/fedora-java/jurand
Vcs: https://github.com/fedora-java/jurand.git

Source: https://github.com/fedora-java/jurand/archive/%version/%name-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: asciidoctor

%description
The tool can be used for patching .java sources in cases where using sed is
insufficient due to Java language syntax. The tool follows Java language rules
rather than applying simple regular expressions on the source code.

%package -n rpm-macros-%name
Group: Development/Java
Summary: Macros for jurand
Requires: %name

%description -n rpm-macros-%name
Macros for jurand.

%prep
%setup -n %name-%version
mv ./macros/macros.jurand ./macros/jurand
sed -i '/^install_file/ s,macros.jurand,jurand,' ./install.sh

%build
%make_build test-compile manpages

%install
export buildroot=%buildroot
export bindir=%_bindir
export rpmmacrodir=%_rpmmacrosdir
export mandir=%_mandir

./install.sh

sed -i -e 's,\.gz$,*,' target/installed_files

%check
%make test

%files -f target/installed_files
%doc --no-dereference LICENSE NOTICE
%doc README.adoc
%exclude %_rpmmacrosdir/%name

%files -n rpm-macros-%name
%_rpmmacrosdir/%name

%changelog
* Thu Mar 13 2025 Anton Meleshnikov <alton@altlinux.org> 1.3.5-alt2
- Add requires

* Mon Mar 03 2025 Anton Meleshnikov <alton@altlinux.org> 1.3.5-alt1
- Initial build for Sisyphus (thanks OpenMandriva for this spec)
