%define        pkgname sassc

Name:          ruby-%pkgname
Version:       2.2.1
Release:       alt2
Summary:       Use libsass with Ruby!
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sass/sassc-ruby
%vcs           https://github.com/sass/sassc-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch1:        patch-%version.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)
BuildRequires: gem(rake)
BuildRequires: gem(rake-compiler)
BuildRequires: gem(rake-compiler-dock)
BuildRequires: gem(pry)
BuildRequires: gem(minitest)
#BuildRequires: gem(minitest-around)
#BuildRequires: gem(test_construct)
BuildRequires: libsass
BuildRequires: libsass-devel

Requires:      libsass
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
This gem combines the speed of libsass, the Sass C implementation, with
the ease of use of the original Ruby Sass library.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup
%patch1 -p1
# TODO: process with setup, by verifying .gitmodules and linking -devel to it without .so
ln -s /usr/include/ ext/libsass/
ln -s /usr/lib64/pkgconfig/libsass.pc ext/libsass/

%build
%ruby_build --srcdldirs=

%install
%ruby_install
rm -f %buildroot%ruby_gemlibdir/ext

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%post
rm -f %ruby_gemlibdir/ext
mkdir %ruby_gemlibdir/ext
ln -s $(find /usr -name libsass.so.1 2>/dev/null) %ruby_gemlibdir/ext/libsass.so


%changelog
* Fri Nov 08 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt2
- changed (*) spec to use build requires
- fixed (!) lost link to system's .so lib (closes #37433)
- fixed (!) requires

* Thu Sep 26 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- update (^) 2.0.0 -> 2.2.1
- update (^) Ruby Police 2.0

* Wed Sep 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.12.1-alt1
- New version.
- Disable tests.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.12.0-alt1
- New version.
- Package as gem.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.11.4-alt1
- Initial build for Sisyphus
