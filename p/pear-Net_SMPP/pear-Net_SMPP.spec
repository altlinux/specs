# spec file for PEAR PHP package Net_SMPP
#

%define pear_name Net_SMPP

Name: pear-%pear_name
Version: 0.4.5
Release: alt1

Summary: PHP/PEAR class for SMPP v3.4 protocol implementation

License: PHP License 3.0
Group: Development/Other
Url: http://pear.php.net/package/Net_SMPP
#Url: https://github.com/pear/Net_SMPP

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %pear_name-%version.tar

BuildArch: noarch

BuildRequires(pre): pear-core rpm-build-pear
Requires: pear-core pear-Net_Socket

%description
PHP PEAR class Net_SMPP is an implementation of the SMPP (Short
Message Peer-to-Peer) v3.4 protocol. SMPP is an open protocol
used in the wireless industry to send and recieve SMS messages.

Net_SMPP does not provide a SMPP client or server, but they can
easily be built with it.

%prep
%setup -n %pear_name-%version

mkdir %pear_name-%version

mv -- Net docs %pear_name-%version/

# Fix md5 sums:
sed -e 's/5a3f7691cee306adc8b2eaf645401426/d134d6824cc5625de57f1fe6b4970c4d/' -i package.xml
sed -e 's/d6e064f95ebaa0febe797adf3a26ad73/fdb54558be96eb0e9d6305d822105cd7/' -i package.xml
sed -e 's/c4380adfa8466a6b2618078d809a96d5/3122ceca4754cafca70a4272437f1ed1/' -i package.xml
sed -e 's/0bcbaf92cc13718807de1e63929552ff/390a6f9b04e1e82be0dd751a82c1b47b/' -i package.xml
sed -e 's/361b4c25e108ae95ce7c6c05aa273676/112b66b25703ca8cc82c58ada337f8ed/' -i package.xml
sed -e 's/381262ac21b17b795b3983310eeea1a2/c6381e4e677238490ebfee0cae4e59bf/' -i package.xml
sed -e 's/b6409d60edd8236d274de466979f6933/c6e8be41ef66cc97bc04d83e564724db/' -i package.xml
sed -e 's/1ee743202be18b9d5d46b48e9b0f1da5/a3af44d07f31605086ec1f8c16655a42/' -i package.xml
sed -e 's/0e35d3f888c40f07b66d1ae4e9e4ea65/b046f2665799baec6bb237a633acb75c/' -i package.xml
sed -e 's/92f255c11b44cc01ec630060d2afb8ae/cdf3460886d44916e6dd98eb4209e983/' -i package.xml
sed -e 's/08982f6f2bdeb60800826f27e2b1696e/a4d02b82c0eedea80bd9de7421260b16/' -i package.xml
sed -e 's/9cfd2f23ca07d452f49d545060bb0391/73bfd5f0f049b87cfb2f5ee82afd49f6/' -i package.xml
sed -e 's/ad3544f6305dc1f2ef5119ae03deca9a/d4b97c855dd4f773863c071f82ed9d4b/' -i package.xml
sed -e 's/8094ac012d0f516ebfd9b0f181c3e8a5/2dd453c346947501011af5e327ac62cd/' -i package.xml
sed -e 's/0d44c664666b0750352c35712625e21b/de7619357f64e37235d0cb78f99594dc/' -i package.xml
sed -e 's/12f3268e627e351d11662f0c7e758a4a/1707dcd973c4ee19a3b3c4a986be64f5/' -i package.xml
sed -e 's/85611293cce8d7621ac40b338eee199d/a31c4d9c5333e9d491412c3745d1bc0d/' -i package.xml
sed -e 's/8b6c76adf91188f5966e3629f4f00c0b/1a478221be32c646444b5804105bd4f8/' -i package.xml
sed -e 's/43508f3ac2846837de8e6c02e4082f04/78f31e63ca722799f2b8c853f06f1d7b/' -i package.xml
sed -e 's/3e40cb57ed1473ddf4a6528e1ec0b846/8c2936d93a9134747575c9b45359e25b/' -i package.xml
sed -e 's/6d7d92cc2fbfc8c6580af4d15a5a11fb/237ec42625a6756904863d2a6174ad66/' -i package.xml

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc CHANGELOG LICENSE
%pear_xmldir/%pear_name.xml
%pear_dir/Net*
%pear_dir/docs*

%changelog
* Fri Aug 10 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.5-alt1
- initial build for ALT Linux Sisyphus
