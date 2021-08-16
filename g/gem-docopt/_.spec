%define        gemname docopt

Name:          gem-docopt
Version:       0.6.1.1
Release:       alt1
Summary:       Parse command line arguments from nothing more than a usage message
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/docopt/docopt.rb
Vcs:           https://github.com/docopt/docopt.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         version.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(json) >= 1.6 gem(json) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency json >= 2.3.0,json < 3
Provides:      gem(docopt) = 0.6.1.1


%description
Isn't it awesome how `optparse` and other option parsers generate help and
usage-messages based on your code?! Hell no! You know what's awesome? It's when
the option parser *is* generated based on the help and usage-message that you
write in a docstring! That's what docopt does!


%package       -n gem-docopt-doc
Version:       0.6.1.1
Release:       alt1
Summary:       Parse command line arguments from nothing more than a usage message documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета docopt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(docopt) = 0.6.1.1

%description   -n gem-docopt-doc
Parse command line arguments from nothing more than a usage message
documentation files.

Isn't it awesome how `optparse` and other option parsers generate help and
usage-messages based on your code?! Hell no! You know what's awesome? It's when
the option parser *is* generated based on the help and usage-message that you
write in a docstring! That's what docopt does!

%description   -n gem-docopt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета docopt.


%package       -n gem-docopt-devel
Version:       0.6.1.1
Release:       alt1
Summary:       Parse command line arguments from nothing more than a usage message development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета docopt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(docopt) = 0.6.1.1
Requires:      gem(json) >= 1.6 gem(json) < 3

%description   -n gem-docopt-devel
Parse command line arguments from nothing more than a usage message development
package.

Isn't it awesome how `optparse` and other option parsers generate help and
usage-messages based on your code?! Hell no! You know what's awesome? It's when
the option parser *is* generated based on the help and usage-message that you
write in a docstring! That's what docopt does!

%description   -n gem-docopt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета docopt.


%prep
%setup
%patch -p1

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

%files         -n gem-docopt-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-docopt-devel
%doc README.md


%changelog
* Mon Jun 28 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.1.1-alt1
- ^ 0.6.1 -> 0.6.1[1]

* Tue Mar 03 2020 Pavel Vasenkov <pav@altlinux.org> 0.6.1-alt2
- + add_python3_path

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- + packaged gem with usage Ruby Policy 2.0
