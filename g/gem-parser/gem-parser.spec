%define        pkgname parser

Name:          gem-%pkgname
Version:       2.6.4.1
Release:       alt1
Summary:       A Ruby parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/whitequark/parser
%vcs           https://github.com/whitequark/parser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)

%description
Parser is a production-ready Ruby parser written in pure Ruby. It recognizes as
much or more code than Ripper, Melbourne, JRubyParser or ruby_parser, and is
vastly more convenient to use.

You can also use unparser to produce equivalent source code from Parser's ASTs.


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.

%package       -n ruby-parse
Summary:       Executable file for rubocop.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n ruby-parse
Executable file for %pkgname.

%description   -n ruby-parse -l ru_RU.UTF-8
Исполнямки для "%pkgname".

%prep
%setup

%build
%ruby_build --use=parser --alias=parse

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n ruby-parse
%_bindir/*


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.6.4.1-alt1
- ^ v2.6.4.1

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 2.6.2.0-alt1
- ^ v2.6.2.0

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 2.6.0.0-alt1
- + initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0
