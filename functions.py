import asyncio

async def claimCheck(message):
    args = message.embeds[0].description.splitlines()

    if args[len(args)-1] == 'React with any emoji to claim!':        #if it is normal react

        end = 3
        kakI = len(args) - 2

        for i in range(3, len(args[kakI])):

            if args[kakI][i] == '*':
                end = i
                break

        args[kakI] = int(args[kakI][2:end])

        if args[kakI] >= 250:

            #claim it if kakera value is high enough

            await asyncio.sleep(0.8)
            await message.add_reaction('👍')
            print('we did it!')
    
    else:  #it is heart react, or there is nothing. kakera val is at the end. We need a condition to see if this is even a roll.
        
        end = 3
        kakI = len(args) - 1

        for i in range(3, len(args[kakI])):

            if args[kakI][i] == '*':
                end = i
                break

        try:

            args[kakI] = int(args[kakI][2:end])

        except: #this is not a roll

            return

        if args[kakI] >= 250:

            #claim it if kakera value is high enough
            
            await asyncio.sleep(0.8)

            if message.reactions: #if heart react
                
                for i in message.reactions:

                    i = i.emoji
                    await message.add_reaction(i)
                    
                print('we did it!')

            else: #if not heart react

                await message.add_reaction('👍')
                print('we did it!')