import hou
def objCreator():
    try:
        n = hou.selectedNodes()[0]
        path = n.parent().path()
        #print n.name()

        choice = hou.ui.displayMessage('Select object to create:', buttons=('Box', 'Sphere', 'PolySphere', 'High Poly sphere'))
        p = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
        position = p.selectPosition()

        if choice == 0:
            
            box = hou.node(path).createNode('box', 'BOX')
            box.setPosition(position)
            box.setDisplayFlag(True)
            box.setRenderFlag(True)

        if choice == 1:
            
            sphere = hou.node(path).createNode('sphere', 'Point_Sphere')
            sphere.setPosition(position)
            sphere.setDisplayFlag(True)
            sphere.setRenderFlag(True)

        if choice == 2:
            
            polysphere = hou.node(path).createNode('sphere', 'Poly_Sphere')
            polysphere.parm('type').set(1)
            polysphere.setPosition(position)
            polysphere.setDisplayFlag(True)
            polysphere.setRenderFlag(True)

        if choice == 3:
            
            hpsphere = hou.node(path).createNode('sphere', 'High_Poly_Sphere')
            hpsphere.parm('type').set(1)
            hpsphere.parm('freq').set(25)
            hpsphere.setPosition(position)
            hpsphere.setDisplayFlag(True)
            hpsphere.setRenderFlag(True)

    except:
        hou.ui.displayMessage('Please select any node on the current context first!')