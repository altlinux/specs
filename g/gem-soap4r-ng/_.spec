%define        gemname soap4r-ng

Name:          gem-soap4r-ng
Version:       2.0.4
Release:       alt1
Summary:       Soap4R-ng - Soap4R (as maintained by RubyJedi) for Ruby 1.8 thru 2.1 and beyond
License:       Ruby
Group:         Development/Ruby
Url:           http://rubyjedi.github.io/soap4r/
Vcs:           https://github.com/rubyjedi/soap4r.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(soap4r-ng) = 2.0.4

%description
Soap4R NextGen (as maintained by RubyJedi) for Ruby 1.8 thru 2.1 and beyond


%package       -n soap4r-ng
Version:       2.0.4
Release:       alt1
Summary:       Soap4R-ng - Soap4R (as maintained by RubyJedi) for Ruby 1.8 thru 2.1 and beyond executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета soap4r-ng
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(soap4r-ng) = 2.0.4

%description   -n soap4r-ng
Soap4R-ng - Soap4R (as maintained by RubyJedi) for Ruby 1.8 thru 2.1 and beyond
executable(s).

Soap4R NextGen (as maintained by RubyJedi) for Ruby 1.8 thru 2.1 and beyond

%description   -n soap4r-ng -l ru_RU.UTF-8
Исполнямка для самоцвета soap4r-ng.


%package       -n gem-soap4r-ng-doc
Version:       2.0.4
Release:       alt1
Summary:       Soap4R-ng - Soap4R (as maintained by RubyJedi) for Ruby 1.8 thru 2.1 and beyond documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета soap4r-ng
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(soap4r-ng) = 2.0.4

%description   -n gem-soap4r-ng-doc
Soap4R-ng - Soap4R (as maintained by RubyJedi) for Ruby 1.8 thru 2.1 and beyond
documentation files.

Soap4R NextGen (as maintained by RubyJedi) for Ruby 1.8 thru 2.1 and beyond

%description   -n gem-soap4r-ng-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета soap4r-ng.


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

%files         -n soap4r-ng
%_bindir/wsdl2ruby.rb
%_bindir/xsd2ruby.rb

%files         -n gem-soap4r-ng-doc
%ruby_gemdocdir


%changelog
* Fri Apr 23 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.4-alt1
- + packaged gem with Ruby Policy 2.0

