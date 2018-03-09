Name: spirv-headers
Version: 1.1
Release: alt2.rc2%ubt

Summary: Machine-readable files from the SPIR-V registry
License: MIT
Group: Development/C++

Url: https://www.khronos.org/registry/spir-v/
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

Source: https://github.com/KhronosGroup/SPIRV-Headers/archive/vulkan-%version-rc2/SPIRV-Headers-vulkan-%version-rc2.tar.gz

BuildRequires(pre): rpm-build-ubt

%description
This package contains machine-readable files from the SPIR-V
registry. This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry file.

%prep
%setup -n SPIRV-Headers-vulkan-%version-rc2

%install
%__mkdir_p %buildroot%_includedir
%__cp -a include/spirv %buildroot%_includedir/spirv

%files
%doc LICENSE README.md
%_includedir/spirv

%changelog
* Fri Mar 09 2018 Nazarov Denis <nenderus@altlinux.org> 1.1-alt2.rc2%ubt
- RC2

* Sat Apr 15 2017 Nazarov Denis <nenderus@altlinux.org> 1.1-alt1
- Initial release for ALT Linux
