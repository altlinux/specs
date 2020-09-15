%define        pkgname yard

Name:          gem-%pkgname
Version:       0.9.25
Release:       alt1
Summary:       YARD is a Ruby Documentation tool. The Y stands for "Yay!"
License:       MIT
Group:         Development/Ruby
Url:           https://yardoc.org/
Vcs:           https://github.com/lsegal/yard.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
YARD is a documentation generation tool for the Ruby programming language. It
enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n %pkgname
Summary:       Yard, Yardoc, and Yri executables for yard gem
Group:         Documentation
BuildArch:     noarch

%description   -n %pkgname
%summary.

Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemlibdir
%ruby_gemspec

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/*


%changelog
* Tue Sep 15 2020 Pavel Skrylev <majioa@altlinux.org> 0.9.25-alt1
- ^ 0.9.19 -> 0.9.25
- ! spec tags

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.19-alt1
- 0.9.16 -> 0.9.19
- > Ruby Policy 2.0

* Sat Dec 29 2018 Pavel Skrylev <majioa@altlinux.org> 0.9.16-alt1
- Initial build for Sisyphus, packaged as a gem
