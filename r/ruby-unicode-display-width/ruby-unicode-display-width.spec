%define        pkgname unicode-display-width
%define        gemname unicode-display_width

Name:          ruby-unicode-display-width
Version:       1.4.1
Release:       alt1
Summary:       Monospace Unicode character width in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/unicode-display_width
# VCS:         https://github.com/janlelis/unicode-display_width.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar
Patch:         alt-fix-datadir.patch

BuildRequires(pre): rpm-build-ruby

%description
%summary

%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.

%prep
%setup -n %name-%version
#%patch -p1
#mkdir data/%name
#cp data/*gz data/%name

%build
%gem_build

%install
%gem_install

%files
%ruby_gemspecdir/%gemname-%version.gemspec
%ruby_gemslibdir/%gemname-%version
#%_datadir/%name

%files doc
%ruby_gemsdocdir/%gemname-%version

%changelog
* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- Bump to 1.4.1;
- Use Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
