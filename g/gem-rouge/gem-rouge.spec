%define        pkgname  rouge

Name:          gem-%pkgname
Version:       3.3.0
Release:       alt1
Summary:       A pure-ruby code highlighter that is compatible with pygments
License:       ISC
Group:         Development/Ruby
Url:           MIT\Pygment
# VCS:         https://github.com/jneen/rouge.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Rouge is a pure-ruby syntax highlighter. It can highlight 100 different
languages, and output HTML or ANSI 256-color text. Its HTML output is compatible
with stylesheets designed for pygments.

If you'd like to help out with this project, assign yourself something from
the issues page, and send me a pull request (even if it's not done yet!). Bonus
points for feature branches.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%package       -n rougify
Summary:       Executable for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n rougify
Executable for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n rougify
%_bindir/rougify

%changelog
* Mon Apr 29 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
