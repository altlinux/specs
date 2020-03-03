# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname docopt

Name:          gem-%pkgname
Version:       0.6.1
Release:       alt2
Summary:       Parse command line arguments from nothing more than a usage message
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/docopt/docopt.rb
Vcs:           https://github.com/docopt/docopt.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%add_python3_path 

%description
Isn't it awesome how `optparse` and other option parsers generate help and
usage-messages based on your code?! Hell no! You know what's awesome? It's when
the option parser *is* generated based on the help and usage-message that you
write in a docstring! That's what docopt does!


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Tue Mar 03 2020 Pavel Vasenkov <pav@altlinux.org> 0.6.1-alt2
- + add_python3_path

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- + packaged gem with usage Ruby Policy 2.0
