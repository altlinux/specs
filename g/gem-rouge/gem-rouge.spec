%define        gemname rouge

Name:          gem-rouge
Version:       3.26.0
Release:       alt1
Summary:       A pure-ruby code highlighter that is compatible with pygments
License:       MIT or BSD-2-Clause
Group:         Development/Ruby
Url:           http://rouge.jneen.net/
Vcs:           https://github.com/jneen/rouge.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rouge) = 3.26.0


%description
Rouge is a pure-ruby syntax highlighter. It can highlight 100 different
languages, and output HTML or ANSI 256-color text. Its HTML output is compatible
with stylesheets designed for pygments.

If you'd like to help out with this project, assign yourself something from the
issues page, and send me a pull request (even if it's not done yet!). Bonus
points for feature branches.


%package       -n rougify
Version:       3.26.0
Release:       alt1
Summary:       A pure-ruby code highlighter that is compatible with pygments executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rouge
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rouge) = 3.26.0

%description   -n rougify
A pure-ruby code highlighter that is compatible with pygments
executable(s).

Rouge is a pure-ruby syntax highlighter. It can highlight 100 different
languages, and output HTML or ANSI 256-color text. Its HTML output is compatible
with stylesheets designed for pygments.

If you'd like to help out with this project, assign yourself something from the
issues page, and send me a pull request (even if it's not done yet!). Bonus
points for feature branches.

%description   -n rougify -l ru_RU.UTF-8
Исполнямка для самоцвета rouge.


%package       -n gem-rouge-doc
Version:       3.26.0
Release:       alt1
Summary:       A pure-ruby code highlighter that is compatible with pygments documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rouge
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rouge) = 3.26.0

%description   -n gem-rouge-doc
A pure-ruby code highlighter that is compatible with pygments documentation
files.

Rouge is a pure-ruby syntax highlighter. It can highlight 100 different
languages, and output HTML or ANSI 256-color text. Its HTML output is compatible
with stylesheets designed for pygments.

If you'd like to help out with this project, assign yourself something from the
issues page, and send me a pull request (even if it's not done yet!). Bonus
points for feature branches.

%description   -n gem-rouge-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rouge.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n rougify
%_bindir/rougify

%files         -n gem-rouge-doc
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.26.0-alt1
- ^ 3.17.0 -> 3.26.0

* Mon Mar 16 2020 Pavel Skrylev <majioa@altlinux.org> 3.17.0-alt1
- ^ 3.7.0 -> 3.17.0

* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 3.7.0-alt1
- > Ruby Policy 2.0
- ^ 3.3.0 -> 3.7.0

* Mon Apr 29 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
