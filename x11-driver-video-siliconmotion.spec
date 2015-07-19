%define _disable_ld_no_undefined 1

Summary:	X.org driver for Silicon Motion Cards
Name:		x11-driver-video-siliconmotion
Version:	1.7.8
Release:	2
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-siliconmotion-%{version}.tar.bz2
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-siliconmotion is
the X.org driver for Silicon Motion Cards.

%prep
%setup -qn xf86-video-siliconmotion-%{version}
%apply_patches
[ -e configure ] || ./autogen.sh

%build
export CC=gcc
export CXX=g++

%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/siliconmotion_drv.so
%{_mandir}/man4/siliconmotion.*
