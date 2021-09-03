%define        gemname clamp

Name:          gem-clamp
Version:       1.3.2
Release:       alt1
Summary:       a Ruby command-line application framework
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mdub/clamp
Vcs:           https://github.com/mdub/clamp.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names dummy
Provides:      gem(clamp) = 1.3.2


%description
"Clamp" is a minimal framework for command-line utilities.

It handles boring stuff like parsing the command-line, and generating help, so
you can get on with making your command actually do stuff.


%package       -n gem-clamp-doc
Version:       1.3.2
Release:       alt1
Summary:       a Ruby command-line application framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета clamp
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(clamp) = 1.3.2

%description   -n gem-clamp-doc
a Ruby command-line application framework documentation files.

"Clamp" is a minimal framework for command-line utilities.

It handles boring stuff like parsing the command-line, and generating help, so
you can get on with making your command actually do stuff.

%description   -n gem-clamp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета clamp.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-clamp-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.2-alt1
- ^ 1.3.0 -> 1.3.2

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
