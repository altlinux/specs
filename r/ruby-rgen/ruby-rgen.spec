
Name:    ruby-rgen
Version: 0.7.0
Release: alt1

Summary: Ruby Modelling and Generator Framework
Group:   Development/Ruby
License: MIT/Ruby
URL:     https://github.com/mthiede/rgen.git

BuildArch: noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit
BuildRequires: ruby-tool-setup

Source: rgen-%version.tar

%description
RGen is a framework for Model Driven Software Development (MDSD)in Ruby.
This means that it helps you build Metamodels, instantiate Models,
modify and transform Models and finally generate arbitrary textual
content from it.

RGen features include:
* Supporting Ruby 1.8.6, 1.8.7 and 1.9.x
* Metamodel definition language (internal Ruby DSL)
* ECore Meta-metamodel with an ECore instance available for every
  Metamodel
* Generator creating the Ruby metamodel definition from an ECore
  instance
* Transformer creating Ruby metamodel classes/modules from an ECore
  instance
* Instantiation of Metamodels, i.e. creation of Models (e.g. from XML)
* Model builder, internal Ruby DSL
* Model fragmentation over several several files and per-fragment
  caching
* Model Transformation language (internal Ruby DSL)
* Powerful template based generator language (internal Ruby DSL inside
  of ERB)
* UML 1.3 metamodel and XMI 1.1 instantiator included
* ECore XML support (XMI 2.0)
* UML-to-ECore and ECore-to-UML transformation (UML class models)
* Enterprise Architect support (UML1.3/XMI1.1)

%package doc
Summary:   Documentation for %name
Group:     Development/Documentation
Requires:  %name = %version-%release
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -n rgen-%version
# Remove modile with unmet
rm -f lib/mmgen/mmgen.rb
%update_setup_rb

%build
%ruby_config
%ruby_build

%check
%ruby_test_unit -Ilib:test tests

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc README* TODO
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- Initial build for ALT Linux

