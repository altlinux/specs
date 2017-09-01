%define  pkgname aws-sdk

Name: 	 ruby-%pkgname
Version: 2.10.37
Release: alt1

Summary: The official AWS SDK for Ruby
License: Apache-2.0
Group:   Development/Ruby
Url:     https://aws.amazon.com/ru/sdk-for-ruby/

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-ruby-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(kramdown)$/d

%description
The official AWS SDK for Ruby. Provides both resource oriented
interfaces and API clients for AWS services.

%package core
Summary: AWS SDK for Ruby - Core
Group:   Development/Ruby
Requires: ruby-jmespath

%description core
Provides API clients for AWS. This gem is part of the official AWS SDK
for Ruby.

%package resources
Summary: AWS SDK for Ruby - Resources
Group:   Development/Ruby
Requires: %name-core = %EVR

%description resources
Provides resource oriented interfaces and other higher-level
abstractions for many AWS services. This gem is part of the official AWS
SDK for Ruby.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-ruby-%version

# Remove alterantive XML parser engines
rm -f aws-sdk-core/lib/aws-sdk-core/xml/parser/engines/{nokogiri,oga,ox,rexml}.rb

for dir in aws-sdk{,-core,-resources};do
	pushd $dir
	%update_setup_rb
	popd
done

%build
for dir in aws-sdk{,-core,-resources};do
	pushd $dir
	%ruby_config
	%ruby_build
	popd
done

%install
for dir in aws-sdk{,-core,-resources};do
	pushd $dir
	%ruby_install
	popd
done
%rdoc aws-sdk{,-core,-resources}/lib
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
#ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/aws-sdk.rb

%files core
%_bindir/aws.rb
%doc aws-sdk-core/*.json
%doc aws-sdk-core/*.crt
%ruby_sitelibdir/aws-sdk-core*
%ruby_sitelibdir/seahorse*

%files resources
%doc aws-sdk-resources/*.json
%ruby_sitelibdir/aws-sdk-resources*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.37-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.21-alt1
- Initial build for Sisyphus
